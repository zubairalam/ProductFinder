import bs4
import redis
import pickle

class ReadFeeds(object):

    def read_feed(self):
        r = redis.Redis("localhost")

        # read latest downloaded filename stored at the end of feeds_downloaded list
        pickled = pickle.loads(r.lindex('feeds_downloaded', -1))
        file_name = pickled[1]
        prod_id_prefix = pickled[0]

        soup = bs4.BeautifulSoup(open("/vagrant/project/" + file_name), "xml")

        all_products = soup.find_all(
            "prod")  # todo: have to map 'prod' with feed_schema table, as this could be different for different provider

        id_url_list = []

        # pick all (providerid_merchantid_productid,url) in a list
        # make providerid_merchantid_productid string
        for product in all_products[:10]:
            # providerid_merchantid_productid
            id = "{}_{}".format(prod_id_prefix, product["id"])
            url = unicode(str(product.mLink.text), "utf-8")
            r.rpush("products", pickle.dumps((id, url)))
