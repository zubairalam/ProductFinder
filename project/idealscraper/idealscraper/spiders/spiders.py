from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from idealscraper.items import Product

import redis
import pickle

import bs4

def get_urls():
    r = redis.Redis("localhost")
    t = r.lrange('products',0,-1)
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



class PCWorld(Spider):
    name = "pcworld"
    allowed_domains = ["pcworld.com"]
    start_urls = []

    def start_requests(self):
        for id,url in get_urls():
            yield Request(url, callback=self.parse_page, meta={"id":id})

    def parse_page(self, response):
        sel = Selector(response)
        product = Product()

        price = sel.xpath("//div[@class='row product productDetail']/section[@class='description col5']/div[@class='row']/div[@class='productPrices col12 ']/span[@class='currentPrice']/ins/text()").extract()
        product["price"]=price
        # -----------------------------------------------------------------------------------

        tt = sel.xpath("//section[@id='content']/div[@class='mboxDefault'][1]/section/h1[@class='pageTitle']").extract()
        title = getTextNodes(tt[0])
        product["title"] = title
        # -----------------------------------------------------------------------------------

        dd = sel.xpath("//section[@id='longDesc']/div[@class='row']/div[@class='col6'][1]/article/p[1]").extract()
        description = getTextNodes(dd[0])
        product["description"] = description
        # -----------------------------------------------------------------------------------

        image_urls = sel.xpath("//section[@class='productMedias']/div[@id='thumbs']/a[contains(@href,'images')]/@href").extract()
        if len(image_urls)==0:
            image_urls = sel.xpath("//section[@class='productMedias']/div[@id='currentView']/a/img/@src").extract()
        product["image_urls"] = image_urls
        # -----------------------------------------------------------------------------------

        product["image_found"] = True if len(image_urls)>0 else False
        # -----------------------------------------------------------------------------------

        instock = sel.xpath("//div[@class='availability']/a[@class='popInTrigger'][1]/span[@class='available']").extract()
        in_stock = getTextNodes(instock[0])
        product["in_stock"] = in_stock
        # -----------------------------------------------------------------------------------

        product["product_id"] = response.meta["id"]
        # -----------------------------------------------------------------------------------

        if 'redirect_urls' in response.request.meta:
            product['redirect_url'] = response.request.meta["redirect_urls"][0]
        else:
            product['redirect_url'] = "" #todo: should it be done this way?
        # -----------------------------------------------------------------------------------

        if response.url == "http://www.pcworld.com/" or response.url == "http://www.pcworld.com" or response.url == "http://www.pcworld.co.uk/gbuk/index.html":
            product['page_type'] = "Home"

        category_page = sel.xpath("//div[@class='col12 resultList']")
        if category_page:
            product['page_type'] = "Category"
        # -----------------------------------------------------------------------------------

        product["url"] = response.request.url
        # -----------------------------------------------------------------------------------

        print product
        return product


