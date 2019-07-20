# -*- coding: utf-8 -*-
import scrapy


class NameSpider(scrapy.Spider):
    name = 'name'
    allowed_domains = ['youdao.com']
    start_urls = ['http://youdao.com/']

    def parse(self, response):
        pass
