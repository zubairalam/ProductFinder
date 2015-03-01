from scrapy.item import Item, Field

class Product(Item):
    # name of the product
    title = Field()

    # description of the product
    description = Field()

    # price of the product
    price = Field()

    images = Field()

    # product images urls
    image_urls = Field()

    # path where to store downloaded images, set by pipeline
    image_paths = Field()

    # stock availability, boolean
    in_stock = Field()

    # actual product url
    url = Field()

    # if start url is different from redirected url
    redirect_url = Field()

    # product not found on given url
    # not_found = Field()
    # todo: have to find a way to know whether product is found on a page or not

    # product images not found on given url
    image_found = Field()

    # home, category, product page
    page_type = Field()

    # product id = providerid_merchant_id_product_id
    product_id = Field()

