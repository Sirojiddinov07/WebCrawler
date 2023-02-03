from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class Crawling_spider(CrawlSpider):
    name = "spidercrawl"
    allowed_domainsv= ["toscrape.com"]
    start_urls = ['http://books.toscrape.com/']


    rules = (
        Rule(LinkExtractor(allow ='catalogue/category')),
        Rule(LinkExtractor(allow ='catalogue', deny='category'), callback='parse_item'),

    
    )

    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "title": response.css(".price_color h1::text").get(),
            "title": response.css(".availability :: text")[1].get().replace("\n", "").replace(" ", ""),

            
        }