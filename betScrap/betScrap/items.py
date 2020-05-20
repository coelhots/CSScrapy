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
    game_team1Name = scrapy.Field()
    game_team1Result = scrapy.Field()
    game_team2Name = scrapy.Field()
    game_team2Result = scrapy.Field()
    game_info = scrapy.Field()
    pass
