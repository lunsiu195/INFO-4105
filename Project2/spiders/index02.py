import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from Project2.items import StackItem
from scrapy import Spider



class proSpider(CrawlSpider):
    name = 'index02'
    allowed_domains = ['cnn.com']
    start_urls = ['https://www.cnn.com/']
    
    rules = (
        Rule(LinkExtractor(allow = 'sport'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow ='us'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'world'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'business'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'politics'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'opinions'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'health'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'entertainment'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'travel'), follow=True, callback="parse_item"),
        Rule(LinkExtractor(allow = 'videos'), follow=True, callback="parse_item"),
    )
    
    def parse_item(self, response):
        item = StackItem()
        for info in response.xpath('//div[@class="headline__wrapper"]'):
            item['name'] = info.xpath('normalize-space(.//h1[@class="headline__text inline-placeholder"]/text())').get()
            item['url'] = response.url
            yield item
            