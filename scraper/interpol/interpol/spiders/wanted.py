import scrapy
from ..items import InterpolItem
import datetime


class WantedSpider(scrapy.Spider):
    name = "wanted"

    def start_requests(self):
        yield scrapy.Request(
            "https://www.interpol.int/How-we-work/Notices/View-Red-Notices",
            callback=self.search_by_nationalities
        )

    def search_by_nationalities(self, response):
        data = response.xpath(
            "//select[@id='arrestWarrantCountryId']/option/@value"
        ).getall()
        for d in data:
            yield scrapy.Request(
                f"https://ws-public.interpol.int/notices/v1/red?arrestWarrantCountryId={d}&resultPerPage=160&page=1",
                callback=self.final_parse
            )

    def final_parse(self, response):
        data = response.json()
        if data["total"] > 160:
            country = data["query"]["arrestWarrantCountryId"]
            for i in range(18,100):
                yield scrapy.Request(f"https://ws-public.interpol.int/notices/v1/red?&ageMin={i}&ageMax={i}&arrestWarrantCountryId={country}", callback=self.detailed_filter)
        else:
            for d in data["_embedded"]["notices"]:
                item = InterpolItem()
                item["forename"] = d.get("forename")
                item["name"] = d.get("name")
                item["date_of_birth"] = d.get("date_of_birth")
                item["entity_id"] = d.get("entity_id")
                try:
                    item["thumbnail"] = d.get("_links").get("thumbnail").get("href")
                except:
                    item["thumbnail"] = None
                entity_id = d.get('entity_id').replace('/','-')
                item["url"] = f"https://www.interpol.int/How-we-work/Notices/View-Red-Notices#{entity_id}"
                item["date"] = datetime.datetime.now()
                yield item

    def detailed_filter(self, response):
        data = response.json()
        for d in data["_embedded"]["notices"]:
            item = InterpolItem()
            item["forename"] = d.get("forename")
            item["name"] = d.get("name")
            item["date_of_birth"] = d.get("date_of_birth")
            item["entity_id"] = d.get("entity_id")
            try:
                item["thumbnail"] = d.get("_links").get("thumbnail").get("href")
            except:
                item["thumbnail"] = None
            entity_id = d.get('entity_id').replace('/','-')
            item["url"] = f"https://www.interpol.int/How-we-work/Notices/View-Red-Notices#{entity_id}"
            item["date"] = datetime.datetime.now()
            yield item
