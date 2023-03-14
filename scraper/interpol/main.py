from interpol.spiders import wanted
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import schedule
import time
import os


def run():
    print("Crawler Process started")
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(wanted.WantedSpider)
    process.start()

schedule.every(int(os.environ.get("SCRAPE_EVERY_MINUTE"))).minutes.do(run)

while True:
    schedule.run_pending()
    time.sleep(5)
