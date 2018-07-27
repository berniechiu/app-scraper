from scrapy.exporters import JsonItemExporter

class JsonPipeline(object):
    def __init__(self):
        self.file = open("apps.json", 'wb')
        self.exporter = JsonItemExporter(
            self.file, encoding='utf-8', ensure_ascii=False, indent=2)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
