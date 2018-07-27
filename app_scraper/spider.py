from app_scraper.csv_reader import CSVReader
import scrapy


class AppStoreScraper(scrapy.Spider):
    name = 'appstore_scraper'

    LANGUAGES_SELECTOR = "//div[contains(@class, 'information-list__item') and dt[contains(text(), 'Languages')]]//dd//span//text()"
    APP_IDENTIFIER_SELECTOR = "//meta[contains(@name, 'apple:content_id')]//@content"
    MINIMUM_VERSION_SELECTOR = "//div[contains(@class, 'information-list__item') and dt[contains(text(), 'Compatibility')]]//dd//span//text()"
    VERSION_REGEX = r'[0-9]+\.[0-9]+'

    def start_requests(self):
        for row in CSVReader.parse_apps():
            yield scrapy.Request(url=row['App Store URL'], callback=self.parse, meta={ 'App Name': row['App Name'] })

    def parse(self, response):
        app_data = {
            'languages': response.selector.xpath(self.LANGUAGES_SELECTOR).extract_first().split(', '),
            'app_identifier': int(response.selector.xpath(self.APP_IDENTIFIER_SELECTOR).extract_first()),
            'name': response.meta['App Name'],
            'minimum_version': response.selector.xpath(self.MINIMUM_VERSION_SELECTOR).re_first(self.VERSION_REGEX)
        }
        return app_data


