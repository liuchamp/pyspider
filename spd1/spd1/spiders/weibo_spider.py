from scrapy.spiders import Spider


class WeiBoSpider(Spider):
    name = 'weibolocl'
    start_urls = "https://news.sina.com.cn/"

    def parse(self, response):
        titles = response.xpath('//div[3]/ul/li/a').extract()
        for ts in titles:
            print(ts)
