from django.core.management.base import BaseCommand
from spiders.spiders import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        # spider spider_name
        print args,len(args)
        if len(args)<1:
            raise Exception("must enter name of spider to crawl")
        extract_all(args[0])