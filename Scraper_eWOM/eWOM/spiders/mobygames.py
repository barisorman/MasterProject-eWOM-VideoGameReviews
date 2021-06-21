import scrapy

class MobygamesSpider(scrapy.Spider):
    name = 'mobygames'
    allowed_domains = ['mobygames.com']
    start_urls = [
        'https://www.mobygames.com/browse/games/psp/',
        'https://www.mobygames.com/browse/games/ps-vita/',
        'https://www.mobygames.com/browse/games/playstation/',
        'https://www.mobygames.com/browse/games/ps2/',
        'https://www.mobygames.com/browse/games/ps3/',
        'https://www.mobygames.com/browse/games/playstation-4/',
        'https://www.mobygames.com/browse/games/playstation-5/',
        'https://www.mobygames.com/browse/games/xbox/',
        'https://www.mobygames.com/browse/games/xbox360/',
        'https://www.mobygames.com/browse/games/n64/',
        'https://www.mobygames.com/browse/games/wii/',
        'https://www.mobygames.com/browse/games/wii-u/',
        'https://www.mobygames.com/browse/games/gamecube/',
        'https://www.mobygames.com/browse/games/gameboy-advance/',
        'https://www.mobygames.com/browse/games/3ds/',
        'https://www.mobygames.com/browse/games/dreamcast/',
        'https://www.mobygames.com/browse/games/xbox-one/',
        'https://www.mobygames.com/browse/games/switch/',
        'https://www.mobygames.com/browse/games/windows/',
        'https://www.mobygames.com/browse/games/iphone/',
        'https://www.mobygames.com/browse/games/stadia/',
        'https://www.mobygames.com/browse/games/xbox-series/'
        ]

    #loop through the games list of each console
    def parse(self, response):
        for url in response.css('td > div > ul > li > a::attr(href)').getall():
            yield scrapy.Request(url=url, callback=self.parse_credits)

    #link to credits page
    def parse_credits(self, response):
        creditslink = response.css('#main > div > div.rightPanelHeader > ul > li:nth-child(2) > a::attr(href)').get()
        yield scrapy.Request(url=creditslink, callback=self.parse_details)

    #the function and selectors for the variables
    def parse_details(self, response):
        yield {
            'Game': str(response.xpath('//*[@id="main"]/div/div[2]/h1/a/text()').get()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Publisher': str(response.xpath('//*[@id="coreGameRelease"]/div[2]/a/text()').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Developer': str(response.xpath('//*[@id="coreGameRelease"]/div[4]/a/text()').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Release Date': str(response.css('#coreGameRelease > div:nth-child(6) > a::text').extract()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Platforms': str(response.xpath('//*[@id="coreGameRelease"]/div[8]/a/text()').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'ESRB Rating': str(response.css('#coreGameGenre > div:nth-child(2) > div:nth-child(2) > a::text').get()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Genre': str(response.xpath('//*[@id="coreGameGenre"]/div/div[2]/a/text()').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Perspective': str(response.css('#coreGameGenre > div > div:nth-child(4) > a::text').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Visual': str(response.css('#coreGameGenre > div > div:nth-child(6) > a::text').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Gameplay': str(response.css('#coreGameGenre > div > div:nth-child(8) > a::text').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Interface': str(response.css('#coreGameGenre > div > div:nth-child(10) > a:nth-child(1)::text').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Setting': str(response.css('#coreGameGenre > div:nth-child(2) > div:nth-child(10) > a::text').getall()).strip().replace("\\xa0","").replace("[","").replace("]","").replace("'",""),
            'Credits': str(response.css('#main > div > div.row > div.col-md-4.col-lg-4 > div.sideBar > div.sideBarContent > div > a::text').getall()).strip().replace("\\xa0"," ").replace("[","").replace("]","").replace("'","")
        }