# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TrendsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    id = Field()
    lp = Field()
    hp = Field()
    beds = Field()
    baths = Field()
    street = Field()
    city = Field()
    state = Field()
    zipcode = Field()
    contact = Field()
    ls = Field()
    hs = Field()
    deposit = Field()
    timestamp = Field()
