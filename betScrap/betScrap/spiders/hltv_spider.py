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
        game_info = response.css('.preformatted-text::text').extract()
        ################
        game_team1Name = response.css('.team1-gradient .teamName::text').extract()
    
        if response.css('.team1-gradient .won::text').extract():
            game_team1Result = response.css('.team1-gradient .won::text').extract()
        else:
            game_team1Result = response.css('.team1-gradient .lost::text').extract()   

        ################  
        game_team2Name = response.css('.team2-gradient .teamName::text').extract()

        if response.css('.team2-gradient .won::text').extract():
            game_team2Result = response.css('.team2-gradient .won::text').extract()
        else:
            game_team2Result = response.css('.team2-gradient .lost::text').extract()

        ################  

        
        
       
        ###   ITEMS   ###
        items['game_date'] = game_date
        items['game_time'] = game_time
        items['game_team1Result'] = game_team1Result
        items['game_team1Name'] = game_team1Name
        items['game_team2Result'] = game_team2Result
        items['game_team2Name'] = game_team2Name
        items['game_info'] = game_info
        ###   ITEMS   ###

    
        yield items

