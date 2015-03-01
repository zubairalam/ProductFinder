from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from django.conf import settings
import os,sys
path=os.path.join(settings.BASE_DIR,"idealscraper")
sys.path.append(path)
import redis
import pickle
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.Redis("localhost")
        pickled_products = r.lrange("scraped_products",0,-1)
        products = []
        es = Elasticsearch()

        # modify the mapping first, to make _id=product_id
        url = "http://localhost:9200/products/product/_mapping"
        mapping = {
            "product": {
                "_id": {
                    "path": "product_id", "index": "not_analyzed", "store": "true"
                }
            }
        }
        response = requests.put(url,mapping)

        for product in pickled_products:
            p = pickle.loads(product)
            res = es.index(index="products", doc_type="product", id=p["product_id"], body=dict(p))
