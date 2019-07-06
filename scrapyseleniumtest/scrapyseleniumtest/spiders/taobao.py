# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapyseleniumtest.items import ProductItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        pass
