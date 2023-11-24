import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_engine.items import CrawledPageItem

class WikipediaCrawlerSpider(scrapy.Spider):
    name = "wikipedia_crawler"
    allowed_domains = ['cnn.com']
    start_urls = ["https://www.cnn.com/"]

    rules = (
        Rule(LinkExtractor(allow=('sport', 'us', 'world', 'business', 'politics', 'opinions', 'health', 'entertainment', 'travel', 'videos')), 
             follow=True, callback="parse_item"),
    )

    def parse(self, response):
        item = CrawledPageItem()
        for article_link in response.xpath('//div[@class="headline__wrapper"]'):
            item['title'] = info.xpath('normalize-space(.//h1[@class="headline__text inline-placeholder"]/text())').get()
            item['url'] = response.url
            

            yield item

        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
