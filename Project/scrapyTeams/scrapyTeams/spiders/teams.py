import scrapy


class TeamsSpider(scrapy.Spider):
    name = "teams"
    start_urls = [
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/america.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/atleticogoianiense.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/atleticomineiro.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/atleticoparanense.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/avai.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/botafogo.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/bragantino.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/ceara.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/corinthians.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/coritiba.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/cuiaba.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/flamengo.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/fluminense.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/fortaleza.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/goias.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/internacional.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/palmeiras.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/santos.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/saopaulo.html',
        'file:///E:/Gabriel/Cadeiras/Dados/html_files/juventude.html',
    ]
    """
    def parse(self, response):
        for jogador in response.css('#all_stats_standard th a'):
            yield{
                'jogador': jogador.css('a::text').get(),
                'posicao': jogador.css('.poptip+ td::text').get(),
            }
    """
    def parse(self, response):
        '''
        #Relativo aos jogadores de "ataque" em geral
        for jogador in range(len(response.css('#all_stats_standard th a'))):
            yield{
                'jogador': response.css('#all_stats_standard th a::text').getall()[jogador],
                'nacao': response.css('#all_stats_standard a > span::text').getall()[jogador],
                'posicao': response.css('.poptip+ td::text').getall()[jogador],
                'idade': response.css('#all_stats_standard .center+ td.center::text').getall()[jogador][:2],
                'minPor90': response.css('#all_stats_standard .right:nth-child(8)::text').getall()[jogador],
                'gols': response.css('#all_stats_standard .right:nth-child(9)::text').getall()[jogador],
                'assist': response.css('#all_stats_standard .right:nth-child(10)::text').getall()[jogador],
            }

        '''
        #Relativo aos goleiros em geral
        for jogador in range(len(response.css('#all_stats_keeper th a'))):
            yield{
                'jogador': response.css('#all_stats_keeper th a::text').getall()[jogador],
                'nacao': response.css('#all_stats_keeper a > span::text').getall()[jogador],
                'posicao': response.css('#all_stats_keeper .poptip+ td::text').getall()[jogador],
                'idade': response.css('#all_stats_keeper .center+ td.center::text').getall()[jogador][:2],
                'minPor90': response.css('#all_stats_keeper tbody .right:nth-child(8)::text').getall()[jogador],
                'gols_contra': response.css('#all_stats_keeper tbody .group_start:nth-child(9)::text').getall()[jogador],
                'defesas': response.css('#all_stats_keeper tbody .right:nth-child(12)::text').getall()[jogador],
            }
        '''
        #Relativo aos jogadores de "defesa" em geral
        for jogador in range(len(response.css('#all_stats_misc th a'))):
            yield{
                'jogador': response.css('#all_stats_misc th a::text').getall()[jogador],
                'nacao': response.css('#all_stats_misc a > span::text').getall()[jogador],
                'posicao': response.css('#all_stats_misc .poptip+ td::text').getall()[jogador],
                'idade': response.css('#all_stats_misc .center+ td.center::text').getall()[jogador][:2],
                'minPor90': response.css('#all_stats_misc tbody .center+ .right::text').getall()[jogador],
                'desarmes': response.css('#all_stats_misc .right:nth-child(14)::text').getall()[jogador],
            }
        '''