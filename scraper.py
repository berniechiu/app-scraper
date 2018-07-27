from scrapy.crawler import CrawlerProcess
from app_scraper.spider import AppStoreScraper

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'ITEM_PIPELINES': {'app_scraper.pipelines.JsonPipeline': 0}
})
process.crawl(AppStoreScraper)
process.start()
