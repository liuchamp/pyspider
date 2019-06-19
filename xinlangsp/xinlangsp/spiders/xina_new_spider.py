import scrapy
from bs4 import BeautifulSoup
import re


class SinaNewsSpider(scrapy.Spider):
    name = 'xinaspider'
    start_urls = [
        'https://mil.news.sina.com.cn/'
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        tags = soup.find_all('a')
        for tag in tags:
            print(tag.get('href'))
