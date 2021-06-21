import scrapy


class VgchartzSpider(scrapy.Spider):
    name = 'vgchartz'
    allowed_domains = ['vgchartz.com']
    start_urls = [
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PSP&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PS&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PS2&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PS3&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PS4&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PS5&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=XB&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=X360&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=XOne&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=XS&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=N64&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=Wii&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=WiiU&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=GC&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=GBA&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=3DS&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=NS&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=DC&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        'https://www.vgchartz.com/games/games.php?name=&keyword=&console=PC&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&showvgchartzscore=1&shownasales=0&showdeveloper=0&showcriticscore=0&showcriticscore=1&showpalsales=0&showreleasedate=0&showreleasedate=1&showuserscore=0&showuserscore=1&showjapansales=0&showlastupdate=0&showlastupdate=1&showothersales=0&showshipped=0',
        ]

    #for loop is integrated to select each game of the listing content
    #Indexing [27 : 77] of the selector ensures the selection of the games, since additional content share the same structure
    def parse(self, response):
        for videogame in response.css('tr')[27 : 77]:
            item = {
                'Game': str(videogame.css('tr > td > a::text').get()).strip(),
                'Platform' : videogame.css('tr > td > img::attr(alt)').get(),
                'Publisher' : videogame.css('tr > td:nth-child(5)::text').get(),
                'VGChartzScore' : videogame.css('tr > td:nth-child(6)::text').get(),
                'CriticScore' : videogame.css('tr > td:nth-child(7)::text').get(),
                'TotalSales' : videogame.css('tr > td:nth-child(9)::text').get(),
                'ReleaseDate' : videogame.css('tr > td:nth-child(10)::text').get(),
                'LastUpdate' : videogame.css('tr > td:nth-child(11)::text').get()
            }
            yield item

        console = response.css('tr:nth-child(4) > td:nth-child(4) > img::attr(alt)').get()

        if console == 'PSP':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PSP&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'PS':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PS&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'PS2':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PS2&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'PS3':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PS3&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'PS4':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PS4&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'PS5':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PS5&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'XB':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=XB&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'X360':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=X360&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'XOne':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=XOne&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'XS':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=XS&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'N64':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=N64&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'Wii':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=Wii&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'WiiU':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=WiiU&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'N64':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=N64&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'GC':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=GC&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'GBA':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=GBA&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == '3DS':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=3DS&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'NS':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=NS&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'DC':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=DC&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)

        elif console == 'PC':
            page_number = int(str(response.css('a.selected::text').get()).replace('\xa0',''))
            if page_number <= 240:
                page_number += 1
            next_page_url = 'https://www.vgchartz.com/games/games.php?page=' + str(page_number) + '&console=PC&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=0&showpalsales=0&showjapansales=0&showothersales=0&showpublisher=1&showdeveloper=0&showreleasedate=1&showlastupdate=1&showvgchartzscore=1&showcriticscore=1&showuserscore=1&showshipped=0'
            yield response.follow(next_page_url, callback=self.parse)