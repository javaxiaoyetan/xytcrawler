# -*- coding: utf-8 -*-

import scrapy
from xytcrawler.city_urls import city_urls_dict
from xytcrawler.items import XytcrawlerItem
import datetime


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = city_urls_dict.values()

    def parse(self, response):
        if response.status == 200:
            url = response.url
            city_code = url[url.rfind('/') + 1:url.rfind('.')]
            item = XytcrawlerItem()
            # 小于101050100说明是直辖市或特别行政区,101320000为香港，101330000为澳门
            if (int(city_code) < 101050100) or (101320000 < int(city_code) < 101340000):
                city = response.xpath('//div[@class="crumbs fl"]/a/text()').extract()[1]
                item['city'] = city
                item['province'] = city
            else:
                province = response.xpath('//div[@class="crumbs fl"]/a/text()').extract()[1]
                city = response.xpath('//div[@class="crumbs fl"]/a/text()').extract()[2]
                item['city'] = city
                item['province'] = province
            item['weather_date'] = datetime.datetime.now()
            lis = response.xpath('//div[@class="t"]/ul[@class="clearfix"]/li')
            item['day'] = lis[0].xpath('.//p[@class="wea"]/text()').extract()
            item['day_temperature'] = lis[0].xpath('.//p[@class="tem"]/span/text()').extract()
            item['sunrise'] = lis[0].xpath('.//p[@class="sun sunUp"]/span/text()').extract()
            item['night'] = lis[1].xpath('.//p[@class="wea"]/text()').extract()
            item['night_temperature'] = lis[1].xpath('.//p[@class="tem"]/span/text()').extract()
            item['sunset'] = lis[1].xpath('.//p[@class="sun sunDown"]/span/text()').extract()
            yield item
