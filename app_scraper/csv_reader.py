import csv
from app_scraper.input_reader import InputReader

class CSVReader:

    @classmethod
    def parse_apps(cls, input_reader=InputReader):
        for filename in input_reader.parse_argv():
            return cls.process_file(filename)

    @classmethod
    def process_file(cls, file):
        with open(file) as csvfile:
            for row in csv.DictReader(csvfile):
                yield row
