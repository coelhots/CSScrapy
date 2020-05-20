# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BetscrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_date = scrapy.Field()
    game_time = scrapy.Field()
    game_teamName1 = scrapy.Field()
    game_won = scrapy.Field()
    game_teamName2 = scrapy.Field()
    game_lost = scrapy.Field()

    pass
