# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    reviews = scrapy.Field()
    rating = scrapy.Field()
    phone = scrapy.Field()
    street_address = scrapy.Field()
    locality = scrapy.Field()
    website = scrapy.Field()
