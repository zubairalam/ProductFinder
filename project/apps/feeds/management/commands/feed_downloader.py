from django.core.management.base import BaseCommand

from apps.feeds.tasks import feed_downloader

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        feed_downloader.delay()
