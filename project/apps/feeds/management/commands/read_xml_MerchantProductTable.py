import bs4
import copy
import re
from urlparse import urlparse

from project.apps.pages.models import *

soup = bs4.BeautifulSoup(open("datafeed_108295.xml"))

all_products = soup.find_all("prod")

# {"id":
# "merchant_id": 
# "name": name
# "description": desc
# "logo":mimage
# "affiliate_url": mlink
# "real_url": <empty initially, updated by scrapy>
# "updated_on": <updated by feed_reader and scrapy>},

fieldname_map = {"name":"name","desc":"description","mimage":"logo","mlink":"affiliate_url"}

product_dict = {"merchant_name": "",
                "merchant_url":"",
                "provider_url":"",
                "provider_name":"",
                "currancy_name":"",
                "category":"",
                "brand_name":"",
                "name": "",
                "description": "",
                "logo": "",
                "affiliate_url": "",
                "real_url": "",
                "updated_on": "",
                "price":""}
# returns links inside document's doctype
def doctype(soup):
    items = [item for item in soup.contents if isinstance(item, bs4.Doctype)]
    return items[0] if items else None

# returns true if product is already available in db
def is_same_product(prod):
    pass


for product in all_products[:2]:
    product_json = copy.deepcopy(product_dict)
    for tag in product.find_all(True):
        try:
            # print str(tag.name.strip()),str(tag.text.strip())
            product_json[fieldname_map[str(tag.name.strip())]] = str(tag.text.strip())
        except:
            pass

    # other fields
    product_json["merchant_name"] = soup.merchant["name"]
    parsed=urlparse(product_json["affiliate_url"])
    product_json["merchant_url"] = parsed.scheme+"://"+parsed.netloc

    # write them to db using product table model.

    # Providers (name,url)
    provider = Providers.objects.filter(name=product_json["provider_name"])
    if len(provider)==0:
        # get provider url, and extract name (domain name) from it
        # a doctype may or many not contain the link for provider, or could contain dtd from 3rd party like w3c.com
        product_json["provider_url"]=""
        product_json["provider_name"]=""
        dt = doctype(soup)
        if dt:
            m=re.search("(?P<url>https?://[^\s]+)",doctype(soup))
            product_json["provider_url"]=m.group("url")
            parsed = urlparse(product_dict)
            product_json["provider_name"]=parsed.netloc

        provider = Providers.objects.create(name=product_json["provider_name"],url=product_json["provider_url"])
        provider.save()

    # Merchant (name,url,provider)
    merchant = Merchants.objects.filter(name=product_json["merchant_name"])
    if len(merchant)==0:
        provider = Providers.objects.get(name=product_json["provider_name"])
        Merchants.objects.create(provider=provider,name=product_json["merchant_name"],url=product_json["merchant_url"])

    # MerchantProducts (merchant,name,desc,stock_status,logo_url,affiliate_url)
    merchant = Merchants.objects.get(name=product_json["merchant_name"])

    # an sku thing is needed, then only we can an update a product if already exists in db.

    # requirements are now changed!!!!!!
    # have to stop here, to start writing another script.






