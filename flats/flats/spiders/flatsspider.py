import scrapy


class FlatsspiderSpider(scrapy.Spider):
    name = "flatsspider"
    allowed_domains = ["om.opensooq.com"]
    start_urls = ["https://om.opensooq.com"]

    def parse(self, response):
        pass