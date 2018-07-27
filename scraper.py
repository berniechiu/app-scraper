import json
from scrapy.crawler import CrawlerProcess
from app_scraper.spider import AppStoreScraper
from app_scraper.filters import Filter, Rule

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'ITEM_PIPELINES': {'app_scraper.pipelines.JsonPipeline': 0}
})
process.crawl(AppStoreScraper)
process.start()

rules = [
    Rule('apps_in_spanish_and_tagalog', 'app_identifier',
        with_rule=lambda app: set(['Spanish', 'Tagalog']).issubset(set(app['languages']))
    ),
    Rule('apps_with_insta_in_name', 'app_identifier',
        with_rule=lambda app: 'insta' in app['name'].lower()
    )
]

with open('apps.json', 'r') as file:
    data = json.load(file)
    app_filters = Filter(rules=rules)
    print app_filters.by_dataset(data)
