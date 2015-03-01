import redis
import pickle

class RedisStorePipeline(object):
    def process_item(self, item, spider):
        # open redis > pickle item > store into a list
        r = redis.Redis("localhost")
        pickled_item = pickle.dumps(item)
        r.rpush("scraped_products",pickled_item)
        return item
