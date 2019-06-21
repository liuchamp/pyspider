# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field()
    pubdate = scrapy.Field()
    score = scrapy.Field()
    synopsis = scrapy.Field()
    celebritys = scrapy.Field()


class DoubanmovieCelebrity(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    role = scrapy.Field()
