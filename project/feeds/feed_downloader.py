import threading
import requests
import urllib2
import gzip
import zipfile
import StringIO
import os
import sys
from datetime import datetime
import pytz

from django.core.validators import  URLValidator
from django.core.exceptions import ValidationError

from django.core.management.base import BaseCommand

from django.conf import settings

from apps.pages.models import Feeds

class FeedDownloader(object):

    # url : source url from where file is requested to download
    # destination : relative path where file is downloaded and saved
    # tries: how many times a url is tried to download

    # todo : total attempt that a thread should take to download a file
    # todo : return status of a download attempt

    def __init__(self,feed,tries):

        self.status = {"url_ok":False,"tries_exceeded":False}
        self.url = feed.url
        self.feed=feed

        # set status
        self.isValidUrl()

    def isValidUrl(self):
        try:
            valid_url = URLValidator()
            valid_url(self.url)
            self.status["url_ok"]=True
        except ValidationError as e:
            self.status["url_ok"] = False
        return self.status["url_ok"]

    # start downloading in a separate thread
    def start_download(self):
        downloader=ThreadedDownloader(self.feed)
        downloader.start()


class ThreadedDownloader(threading.Thread):
    def __init__(self,feed):
        super(ThreadedDownloader,self).__init__()
        self.url = feed.url
        self.auth_tuple=(feed.username,feed.password)
        self.filename = feed.file_name

        self.magic_dict = {
            "\x1f\x8b\x08": "gz",
            "\x42\x5a\x68": "bz2",
            "\x50\x4b\x03\x04": "zip"
        }

        self.max_len = max(len(x) for x in self.magic_dict)

    def file_type(self, filename):
        with open(filename) as f:
            file_start = f.read(self.max_len)
        for magic, filetype in self.magic_dict.items():
            if file_start.startswith(magic):
                return filetype
        return "no match"

    def run(self):
        # download file and save them to static folder
        with open(self.filename, 'wb') as handle:
            response = requests.get(self.url,auth=self.auth_tuple,stream=True)
            handle.write(response.content)

        filetype = self.file_type(self.filename)
        if filetype=="gz":
            g=gzip.open(self.filename,"rb")
            file_content = g.read()
            with open(self.filename,"wb") as f:
                f.write(file_content)
        elif filetype=="zip":
            with zipfile.ZipFile(self.filename,"r") as z:
                name = z.namelist()[0]
                file_name=z.open(name)
                file_content=file_name.read()
                with open(self.filename,"w") as f:
                    f.write(file_content)

class QueryFeeds(object):

    def getFeeds(object):
        feeds = Feeds.objects.all().order_by('scheduled_at')
        # remove feeds whose date time has been passed
        dt_now = datetime.now()
        local_tz = pytz.timezone(settings.TIME_ZONE)
        local_now = local_tz.localize(dt_now)
        local_now_utc = local_now.astimezone(pytz.UTC)

        d_now = local_now_utc.date()
        t_now = local_now_utc.ctime()
        now_hour = local_now_utc.hour
        now_minute = local_now_utc.minute

        valid_feeds = []

        for feed in feeds:
            date = feed.scheduled_at.date()
            hour = feed.scheduled_at.hour
            minute = feed.scheduled_at.minute

            if date == d_now and now_hour == hour and now_minute == minute:
                valid_feeds.append(feed)

        # select those whose date and time are same
        print "valid feeds: {}".format(valid_feeds)
        return valid_feeds

    def getFeedById(self, feed_id):
        feed = None
        try:
            feed = Feeds.objects.get(id=int(feed_id))
        except Exception:
            pass
        return feed