from django.core.management.base import BaseCommand

from apps.feeds.tasks import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        read_products()