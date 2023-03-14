import scrapy


class InterpolItem(scrapy.Item):
    forename = scrapy.Field()
    name = scrapy.Field()
    date_of_birth = scrapy.Field()
    entity_id = scrapy.Field()
    thumbnail = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()