import redis
import pickle

import bs4
import re

from copy import deepcopy

import requests
from urlparse import urlparse
from os.path import splitext, basename

from requests_futures.sessions import FuturesSession

from lxml.html import fromstring
from .items import Item

import threading

from multiprocessing.dummy import Pool as ThreadPool

from django.conf import settings

Images = {"url":"", "path":"", "ok":False}

# def item_images_downloader(pid,images):
#     for image in images:
#         img_d = image_downloader(pid, image)
#         img_d.start()

def image_downloader(pimg):
    image_stream = requests.get(pimg[1]["url"], stream=True)
    if image_stream.status_code == 200:
        # find the file_name and save it using that name
        parts = urlparse(pimg[1]["url"])
        filename = "full_" + str(pimg[0]) + "__" + basename(parts.path)
        pimg[1]["url"] = filename
        print filename, str(pimg[0]),"*"*100
        # save downloaded file with name=filename
        static_dir = settings.STATICFILES_DIRS
        with open(static_dir[0] + "/images/product_images/full/" + filename, "wb") as f:
            for chunk in image_stream.iter_content():
                f.write(chunk)
                pimg[1]["ok"] = True

class ItemImagesDownloader(threading.Thread):
    def __init__(self, pid, images):
        super(ItemImagesDownloader, self).__init__()
        self.pid = pid
        self.images = images

    def run(self):
        for image in self.images:
            img_d = ImageDownloader(self.pid,image)
            img_d.start()

class ImageDownloader(threading.Thread):
    def __init__(self, pid,image):
        super(ImageDownloader, self).__init__()
        self.image = image
        self.pid = pid

    def run(self):
        # this takes the url and start downloading and when download is finished
        # what it shall do.

        image_stream = requests.get(self.image["url"], stream=True)
        if image_stream.status_code == 200:
            # find the file_name and save it using that name
            parts = urlparse(self.image["url"])
            filename = "full/"+str(self.pid)+"__"+basename(parts.path)
            self.image["path"] = filename
            # save downloaded file with name=filename
            static_dir = settings.STATICFILES_DIRS
            with open(static_dir[0]+"/images/product_images/full/"+filename,"wb") as f:
                for chunk in image_stream.iter_content():
                    f.write(chunk)
                self.image["ok"] = True


def get_urls():
    r = redis.Redis("localhost")
    t = r.lrange('products', 0, -1)
    id_urls = []
    for x in t:
        id_urls.append(pickle.loads(x))
    return id_urls


def getTextNodes(html):
    soup = bs4.BeautifulSoup(html)
    txt_nodes = []
    for string in soup.strings:
        txt_nodes.append(string)
    return " ".join("".join(txt_nodes).strip().split())


class PCWorld(object):

    def extract(self, pid, response):

        item = Item()

        page = fromstring(response.content)

        # -----------------------------------------------------------------------------------
        prices = page.xpath(
            "//div[@class='row product productDetail']/section[@class='description col5']/div[@class='row']/div[@class='productPrices col12 ']/span[@class='currentPrice']/ins/text()")
        p = re.search(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?', prices[0])
        try:
            price = p.group(0)
        except:
            price = 0

        item.price = price
        # -----------------------------------------------------------------------------------

        tt = page.xpath("//section[@id='content']/div[@class='mboxDefault'][1]/section/h1[@class='pageTitle']")
        t = tt[0]
        title = getTextNodes(t.text_content())
        item.title = title
        # -----------------------------------------------------------------------------------

        dd = page.xpath("//section[@id='longDesc']/div[@class='row']/div[@class='col6'][1]/article/p[1]")
        d = dd[0]
        description = getTextNodes(d.text_content())
        item.description = description
        # -----------------------------------------------------------------------------------

        # download
        # give the file a name = product_id_product_name_sequence_number
        # save the file with above name in /static/product_images/full/
        # save the image_url and file_name in storage
        # do this after images url have been extracted

        image_urls = page.xpath(
            "//section[@class='productMedias']/div[@id='thumbs']/a[contains(@href,'images')]/@href")
        if len(image_urls) == 0:
            image_urls = page.xpath("//section[@class='productMedias']/div[@id='currentView']/a/img/@src")
        item.images = image_urls
        # -----------------------------------------------------------------------------------

        item.image_found = True if len(image_urls) > 0 else False
        # -----------------------------------------------------------------------------------

        if item.image_found:

            # images_d = ItemImagesDownloader(id, image_urls)
            # images_d.start()

            # list of images from image_urls
            images_list = []
            for url in image_urls:
                images = deepcopy(Images)
                images["url"] = url
                images_list.append((pid,images))



            # pool = ThreadPool(processes=4)
            # results = pool.map(image_downloader, images_list)
            item.images = images_list

        # -----------------------------------------------------------------------------------

        instock = page.xpath(
            "//div[@class='availability']/a[@class='popInTrigger'][1]/span[@class='available']")
        ins = instock[0]
        in_stock = getTextNodes(ins.text_content())
        if "availablility" in in_stock.lower():
            item.in_stock = "in_stock"
        else:
            item.in_stock = "notfound"
        # -----------------------------------------------------------------------------------

        item.product_id = pid
        # -----------------------------------------------------------------------------------

        # if response.status_code in [301,302]:
        # product['redirect_url'] = response.request.meta["redirect_urls"][0]
        # else:
        #     product['redirect_url'] = ""
        # -----------------------------------------------------------------------------------

        if response.url == "http://www.pcworld.com/" or response.url == "http://www.pcworld.com" or response.url == "http://www.pcworld.co.uk/gbuk/index.html":
            item.page_type = "Home"

        category_page = page.xpath("//div[@class='col12 resultList']")
        if category_page:
            item.page_type = "Category"

        if not item.page_type:
            item.page_type = "Default"
        # -----------------------------------------------------------------------------------

        item.url = response.url
        # -----------------------------------------------------------------------------------

        print item.__dict__
        return item

SPIDERS = {"pcworld":PCWorld()}



# entry point for a scraper to start it.
def extract_all(name):

    spider = SPIDERS[name]


    session = FuturesSession(max_workers=10)

    futures=[(pid, session.get(url)) for pid, url in get_urls()]

    future_responses = [(pid, future.result()) for pid, future in futures]

    for pid,response in future_responses:
        spider.extract(pid,response)


def download_images(images):
    # this will download the images and each image will be downloaded asynchronously using workers
    # pass a list of tuples [(id, <image_dict>), ...]

    # have to see if 10 data extracting worker and another 10 image downloading workers, together they work or not


    session = FuturesSession(max_workers=10)

    # pick the urls
    # get futures objects
    # get response objects
    # done!!

    img_futures = [(pid,session.get(img["url"])) for pid,img in images]

    img_responses = [(pid, img_future.result()) for pid,img_future in img_futures]

    # pool = ThreadPool(processes=1)
    #
    # pool.apply_async(save_images, [img_responses])

    # now the next step
    # have to call save images workers


def save_images(images):
    # save each image to folder with a name
    # save their path and other info in db

    pass

def start_scraping(name):
    extract_all()
    # a list should be returned
    # pass that list to download_images

    # suppose
    # all 100000 urls data extracted and in between their images are being downloaded and processed

    # or
    # async download images :: requests_futures
    # async image processing :: some thread, celery, multiprocessing

    # it would be good if
    # we keep extracting the textual data :: this is working
    # images pertaining to a prod_id should be queued to another async workers for downloading :: this is same
    # image processing like saving to hardisk and db should be handled by another async workers :: have to find