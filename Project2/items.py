# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class StackItem(Item):
    name = Field()
    url = Field()


class Project2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
