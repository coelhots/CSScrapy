import scrapy
from ..items import BetscrapItem


class QuotesSpider(scrapy.Spider):
    name = "hltv_spider"
    start_urls = [
        'https://www.hltv.org/results'
    ]

    def parse(self, response):
        for quote in response.css('.contentCol'):
            event_title = quote.css('.results-holder .results-all .event-name::text').getall()
            event_date = quote.css('.results-sublist .standard-headline::text').getall()
            team_won = quote.css('.team-won::text').getall()
            team_won_results = quote.css('.results-holder .results-all .score-won::text').getall()

            yield {
                'event_title': event_title,
                'event_date': event_date,
                'team_won': team_won,
                'team_won_results': team_won_results
            }