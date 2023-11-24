import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from Project2.items import StackItem
from scrapy import Spider



class proSpider(CrawlSpider):
    name = 'index'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/']
    
    rules = (
        Rule(LinkExtractor(allow = 'wiki'), follow=True, callback="parse_item"),
    )
    
    def parse_item(self, response):
        item = StackItem()
        for info in response.xpath('//div[@class="mw-content-container"]'):
            item['name'] = info.xpath('.//h1[@id="firstHeading"]/span[@class="mw-page-title-main"]/text()').get()
            item['url'] = response.url
            yield item