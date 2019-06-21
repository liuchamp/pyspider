# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient


class DoubanmoviePipeline(object):
    collection_name = "doubanmovie"

    def __init__(self, mongo_urls, mongo_database):
        self.mongo_urls = mongo_urls
        self.mongo_database = mongo_database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('MONGO_URLS'),
            crawler.settings.get('MONGO_DATABASENAME')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_urls)
        self.database = self.client[self.mongo_database]
        self.collection = self.database[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
