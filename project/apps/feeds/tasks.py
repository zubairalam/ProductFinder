from __future__ import absolute_import

from celery import shared_task
import redis
import pickle
import os,sys

# from .feed_downloader import *

from feeds.feed_downloader import *
from feeds.feed_reader import *

# from .read_feed import *


@shared_task
def feed_downloader(feed_id):
    feeds = QueryFeeds()
    feed = feeds.getFeedById(feed_id)
    r = redis.Redis('localhost')
    r.rpush('feeds_downloaded', pickle.dumps(t))

    fd = FeedDownloader(feed, tries=3)
    fd.start_download()

@shared_task
def downloader():
    # execute static/shell_scripts/feed_downloader.sh
    import subprocess
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    subprocess.call(PROJECT_PATH+"/static/shell_scripts/feed_downloader.sh", shell=True)

@shared_task
def read_products():
    reader = ReadFeeds()
    reader.read_feed()