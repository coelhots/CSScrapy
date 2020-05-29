import scrapy
from ..items import BetscrapItem


class HLTVSpider(scrapy.Spider):
    name = "hltv_spider"
    page_number = 100
    start_urls = [
        "https://www.hltv.org/results"
    ]

    def parse(self, response):
        results_holder = response.css('.results-holder:not(.results-all)')

        for quote in results_holder.css('.results-sublist'):
            game_date = quote.css('.standard-headline::text').getall()

            for result in quote.css('.result'):
                event_title = result.css('.event-name::text').getall()
                
                team_won = ""
                team_won_score = result.css('.score-won::text').getall()
                team_lost = ""
                team_lost_score = result.css('.score-lost::text').getall()
                best_of = result.css('.map-text::text').getall()
                team1 = result.css('.team1')
                team2 = result.css('.team2')
                if team1.css('.team-won::text').getall():
                    team_won = team1.css('.team-won::text').getall()
                    team_lost = team2.css('.team::text').getall()
                else:
                    team_won = team2.css('.team-won::text').getall()
                    team_lost = team1.css('.team::text').getall()
                    


                yield {
                    'game_date': game_date,
                    'team_won': team_won,
                    'team_won_score': team_won_score,
                    'team_lost': team_lost,
                    'team_lost_score': team_lost_score,                    
                    'event_title': event_title,
                    'best_of': best_of
                }
        next_page = 'https://www.hltv.org/results?offset=' + str(HLTVSpider.page_number)
        if HLTVSpider.page_number <= 55000:
            HLTVSpider.page_number += 100
            yield response.follow(next_page, callback = self.parse)