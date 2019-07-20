# -*- coding: utf-8 -*-
import scrapy


class XiaomiSpider(scrapy.Spider):
    name = 'xiaomi'
    allowed_domains = ['mi.com']
    start_urls = ['http://mi.com/']

    def parse(self, response):
        pass
