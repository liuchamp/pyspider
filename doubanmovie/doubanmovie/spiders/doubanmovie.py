import scrapy
from bs4 import BeautifulSoup
import re
import traceback


class DoubanMovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    start_urls = [
        'https://movie.douban.com/'
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
#        selectors=['//ul/li[@class="ui-slide-item s"]/ul/li[@class="poster"]/a',]
        tags = soup.find_all('a', href=re.compile(r"movie.douban.*\d{8}\/*"))
        for tag in tags:
            url = tag.get('href')
            yield scrapy.Request(url, callback=self.parse_movie_detail)

    def parse_movie_detail(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        try:
            title = self.extract_movie_title(soup)
            if title is None:
                raise Exception('title not find for' + response.url)
            pudb = self.extract_movie_pub_date(soup)
            if pudb is None:
                raise Exception('pubdata is not find for' + response.url)
            print(pudb)
        except Exception as e:
            self.logger.error(str(e))

    def extract_movie_title(self, soup):
        selectors = ['div>h1>span']
        for selector in selectors:
            if len(soup.select(selector)) != 0:
                return soup.select(selector)[0].text

    def extract_movie_pub_date(self, soup):
        tags = soup.find_all('span', property="v:initialReleaseDate", limit=50)
        pudb = ""
        for tag in tags:
            pudb += tag.text
        return pudb
