# Scrapy settings for idealscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'idealscraper'

SPIDER_MODULES = ['idealscraper.spiders']
NEWSPIDER_MODULE = 'idealscraper.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'idealscraper (+http://www.yourdomain.com)'


DEFAULT_ITEM_CLASS = 'idealscraper.items.Product'

ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline',
                  'idealscraper.ImagesPipeline.ProductImagesPipeline',
                  'idealscraper.pipelines.RedisStorePipeline']


# from django.conf import settings
import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

IMAGES_STORE = "/vagrant/project/static/images/product_images"

# IMAGES_STORE =  os.path.join(settings.BASE_DIR, '/static/images/product_images')

meta = {'dont_redirect': True, "handle_httpstatus_list": [301, 302, 303]}
# in case of above http codes, scraper will still scrap things
