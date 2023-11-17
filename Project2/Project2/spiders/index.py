import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class proSpider(CrawlSpider):
    name = 'index'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/']
    
    rules = (
        Rule(LinkExtractor(allow = 'wiki/')),
    )
    
    def parse_doc(self, response):
        yield {
            'title' : response.css('div.pdp-link a::text').get()
        }