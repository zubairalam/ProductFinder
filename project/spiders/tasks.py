from __future__ import absolute_import

from celery import shared_task
import redis
import pickle
import os, sys








@shared_task
def extract_text(name):
    # will extract textual data from a website
    # also fetch the image urls if there is

    pass