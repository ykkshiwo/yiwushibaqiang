# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YiwushibaqiangItem(scrapy.Item):
    review = scrapy.Field()
    problem = scrapy.Field()
    problem_time = scrapy.Field()
    problem_who = scrapy.Field()
    comment = scrapy.Field()
