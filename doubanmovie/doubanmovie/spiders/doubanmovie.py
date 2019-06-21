import scrapy
from bs4 import BeautifulSoup
import re
import traceback
from doubanmovie.items import DoubanmovieItem, DoubanmovieCelebrity


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
            scroce = self.extract_movie_score(soup)
            if scroce is None:
                raise Exception('scroce is not find for' + response.url)
            synopsis = self.extract_movie_synopsis(soup)
            if synopsis is None:
                raise Exception('synopsis is not find for' + response.url)
            celebritys = self.extract_movie_celebrities(soup)
            if celebritys is None:
                raise Exception('celebritys is not find for' + response.url)

        except Exception as e:
            self.logger.error(str(e))

        item = DoubanmovieItem(
            _id=response.url, name=title, pubdate=pudb, score=scroce, synopsis=synopsis, celebritys=celebritys)
        yield item

    def extract_movie_title(self, soup):
        selectors = ['div>h1>span']
        for selector in selectors:
            if len(soup.select(selector)) != 0:
                return soup.select(selector)[0].text

    def extract_movie_pub_date(self, soup):
        tags = soup.find_all('span', property="v:initialReleaseDate", limit=50)
        pudb = []
        for tag in tags:
            pudb.append(tag.text)
        return pudb

    def extract_movie_score(self, soup):
        tag = soup.select_one(
            '#interest_sectl > div.rating_wrap.clearbox > div.rating_self.clearfix > strong')
        return tag.text

    def extract_movie_synopsis(self, soup):
        tag = soup.select_one(
            '#link-report > span')
        return tag.text

    def extract_movie_celebrities(self, soup):
        selector = '#celebrities > ul > li'
        tags = soup.select(selector)
        cs = []
        for tag in tags:
            name = tag.select_one('div > span.name').text
            role = tag.select_one('div > span.role').text
            ics = DoubanmovieCelebrity(name=name, role=role)
            cs.append(ics)
        return cs
