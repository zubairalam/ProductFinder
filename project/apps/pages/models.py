from django.db import models
from djcelery.models import *
from datetime import datetime
from django.conf import settings
import pytz


# record of a provider have to filled manually or from some other source, as provider data is not available in its datafeed
class Providers(models.Model):
    name  = models.CharField(max_length=200)
    description = models.TextField()
    date_joined = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=500)
    logo = models.ImageField(upload_to="provider_logos")
    # logo_url = models.URLField(max_length=500)

    def __unicode__(self):
        return self.name

# url field have to filled manually
class Merchants(models.Model):
    provider = models.ForeignKey(Providers)
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="merchant_logos")
    # logo_url = models.URLField(max_length=500)

    def __unicode__(self):
        return self.name





class Feeds(models.Model):
    periodic_task = models.ForeignKey(PeriodicTask, null=True)
    provider = models.ForeignKey(Providers)
    merchant = models.ForeignKey(Merchants)
    file_name = models.CharField(max_length=100) # i.e. feed.xml.gzip, feed.xml.zip etc.
    url = models.TextField() # urls of feeds are usually too long string, can't depend on max_length, should be a blob.
    username = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    date_added = models.DateTimeField(auto_now=True)
    # scheduled_at = models.DateTimeField()
    successful_download = models.BooleanField(default=0)

    def __unicode__(self):
        return datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def save(self,*args,**kwargs):
        self.file_name = ("{}_{}_{}".format(self.provider.name,self.merchant.name,str(self))).replace(" ","_").replace(":","_")
        # set scheduled_at field taking values from periodic_task's crontab
        # ctab = self.periodic_task.crontab
        # year = int(datetime.today().year)
        # month = datetime.today().month if ctab.month_of_year=="*" else int(ctab.month_of_year)
        # day = datetime.today().day if ctab.day_of_month == "*" else int(ctab.day_of_month)
        # hour = 1 if ctab.hour=="*" else int(ctab.hour)
        # minute = 1 if ctab.minute=="*" else int(ctab.minute)
        # seconds = 0
        # tz=pytz.timezone(settings.TIME_ZONE)
        # dt=tz.localize(datetime(year,month,day,hour,minute,seconds))
        # dt_utc=dt.astimezone(pytz.UTC)
        # self.scheduled_at=dt_utc

        # pass this feed id to the scheduled task downloader
        # pt = eval(self.periodic_task.args)
        # pt.append(self.id)
        # self.periodic_task.args = str(pt)
        # self.periodic_task.save()
        super(Feeds,self).save(*args,**kwargs)


from django.db.models.signals import post_save


def set_feedId(sender, instance=False, **kwargs):
    feed = Feeds.objects.get(id=instance.id)
    pt = feed.periodic_task
    argslist = eval(pt.args)
    argslist.append(instance.id)
    pt.args = str(argslist)
    pt.save()

post_save.connect(set_feedId, sender=Feeds)


# by feed, scrapy
class MerchantProducts(models.Model):
    merchant = models.ForeignKey(Merchants)
    name = models.CharField(max_length=300)
    description = models.TextField()
    stock_status = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="product_logos") # this seems to be trivial, as this is in Multipics
    logo_url = models.URLField(max_length=500,default="http://urlnotgiven.com")
    affiliate_url = models.URLField(max_length=500)
    real_url = models.URLField(max_length=500)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

# class Delivery(models.Model):
#   pass

# by scrapy
class Multipics(models.Model):
    product = models.ForeignKey(MerchantProducts)
    image = models.ImageField(upload_to="product_multipics")
    image_url = models.URLField(max_length=500)
    logo = models.BooleanField(default=0)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '<img src="%s"/>' % self.image_url

# feed, scrapy
# if price of a product is changed a new Price object will be saved under tht product id
class ProductPrice(models.Model):
    product = models.ForeignKey(MerchantProducts)
    price = models.CharField(max_length=10,default="0") #Integer or Float Field ??
    currency_name = models.CharField(max_length=200) # could be managed in other table
    updated_on = models.DateTimeField(auto_now=True)

# feed,scrapy
class Brand(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    url = models.URLField(max_length=400)
    logo = models.ImageField(upload_to="brand_logos")
    # url = models.URLField(max_length=400)


# manual,scrapy
class Features(models.Model):
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=300)

# manual,scrapy
# many2many between product and features
class ProductFeatures(models.Model):
    product = models.ForeignKey(MerchantProducts)
    feature = models.ForeignKey(Features)

# manual,scrapy
class Category(models.Model):
    name = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=400) # list of parent_category_id separated by comma

# manual,scrapy
class ProductCategory(models.Model):
    product = models.ForeignKey(MerchantProducts)
    category = models.ForeignKey(Category)

