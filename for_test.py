import scrapy
from ..items import BetscrapItem


class QuotesSpider(scrapy.Spider):
    name = "hltv_spider"
    start_urls = [
        'https://www.hltv.org/matches/2341154/astralis-vs-g2-esl-one-road-to-rio-europe',
    ]

    def parse(self, response):
        for quote in response.css('div.timeAndEvent'):
            date = quote.css('div.date::text').get()
            time = quote.css('div.time::text').get()
            yield {
                'date': date,
                'time': time
            }
        
        for quote in response.css('.team1-gradient'):
            yield {
                'won': quote.css('.won::text').extract(),
                'teamName': quote.css('div.teamName::text').extract()
            }

        for quote in response.css('.team2-gradient'):
            yield {
                'lost': quote.css('.lost::text').get(),
                'teamName': quote.css('.teamName::text').get()
            }

