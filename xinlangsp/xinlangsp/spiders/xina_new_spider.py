import scrapy
from bs4 import BeautifulSoup
import re


class SinaNewsSpider(scrapy.Spider):
    name = 'xinaspider'
    start_urls = [
        'https://mil.news.sina.com.cn/'
    ]
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        tags = soup.find_all('a', href=re.compile(
            r"sina.*\d{4}-\d{2}-\d{2}.*shtml$"))
        for tag in tags:
            url = tag.get('href')
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        try:
            title = self.extract_title(soup)
            if title is None:
                raise Exception('title not found for' + response.url)
            print(title)
        except Exception as e:
            self.logger.error(str(e))

    def extract_title(self, soup):
        selectors = ['h1.main-title', 'h1.l_tit', 'h1#artibodyTitle']
        for selector in selectors:
            if len(soup.select(selector)) != 0:
                title = soup.select(selector)[0].text
                return title

    def extract_pub_date(self, soup):
        selectors = ['data']
