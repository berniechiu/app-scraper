from app_scraper.csv_reader import CSVReader
import scrapy


class AppStoreScraper(scrapy.Spider):
    name = 'appstore_scraper'

    def start_requests(self):
        for row in CSVReader.parse_apps():
            yield scrapy.Request(url=row['App Store URL'], callback=self.parse)

    def parse(self, response):
        print response.url
