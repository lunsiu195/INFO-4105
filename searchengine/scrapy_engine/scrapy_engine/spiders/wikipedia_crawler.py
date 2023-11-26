import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy_engine.items import CrawledPageItem
from scrapy import Spider

class WikipediaCrawlerSpider(CrawlSpider):
    name = "wikipedia_crawler"
    allowed_domains = ['cnn.com']
    start_urls = ["https://www.cnn.com/"]

    rules = (
        Rule(LinkExtractor(allow=('sport', 'us', 'world', 'business', 'politics', 'opinions', 'health', 'entertainment', 'travel', 'videos')), 
             follow=True, callback="parse_item"),
    )

    def parse_item(self, response):
        item = CrawledPageItem()
        for article_link in response.xpath('//div[@class="headline__wrapper"]'):
            item['title'] = article_link.xpath('normalize-space(.//h1[@class="headline__text inline-placeholder"]/text())').get()
            item['url'] = response.url
            
# Add logging to inspect item
            self.logger.info(f"Scraped item: {item}")

            yield item

        # Follow pagination links
        #next_page = response.css("li.next a::attr(href)").get()
        #if next_page:
            #yield response.follow(next_page, self.parse)
