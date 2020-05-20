import scrapy
from ..items import BetscrapItem


class HLTVSpider(scrapy.Spider):
    name = "hltv_spider"
    start_urls = [
        'https://www.hltv.org/matches/2341154/astralis-vs-g2-esl-one-road-to-rio-europe',
    ]

    def parse(self, response):
        items = BetscrapItem()


        game_date = response.css('.timeAndEvent .date::text').extract()
        game_time = response.css('.timeAndEvent .time::text').extract()
        game_won = response.css('.team1-gradient .won::text').extract()
        game_teamName1 = response.css('.team1-gradient .teamName::text').extract()
        game_lost = response.css('.team2-gradient .lost::text').extract()
        game_teamName2 = response.css('.team2-gradient .teamName::text').extract()

        items['game_date'] = game_date
        items['game_time'] = game_time
        items['game_won'] = game_won
        items['game_teamName1'] = game_teamName1
        items['game_lost'] = game_lost
        items['game_teamName2'] = game_teamName2
        
        yield items

