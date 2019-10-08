# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class  XytcrawlerItem(scrapy.Item):
    weather_date = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    day = scrapy.Field()
    day_temperature = scrapy.Field()
    sunrise = scrapy.Field()
    night = scrapy.Field()
    night_temperature = scrapy.Field()
    sunset = scrapy.Field()
    pass
