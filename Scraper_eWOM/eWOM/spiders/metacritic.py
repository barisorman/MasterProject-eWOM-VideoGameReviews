import scrapy


class CriticReviewsSpider(scrapy.Spider):
    name = 'metacritic'
    allowed_domains = ['metacritic.com']
    start_urls = [
        'https://www.metacritic.com/browse/games/release-date/available/psp/date',
        'https://www.metacritic.com/browse/games/release-date/available/ps/date',
        'https://www.metacritic.com/browse/games/release-date/available/ps2/date',
        'https://www.metacritic.com/browse/games/release-date/available/ps3/date',
        'https://www.metacritic.com/browse/games/release-date/available/ps4/date',
        'https://www.metacritic.com/browse/games/release-date/available/ps5/date',
        'https://www.metacritic.com/browse/games/release-date/available/xbox/date',
        'https://www.metacritic.com/browse/games/release-date/available/xbox360/date',
        'https://www.metacritic.com/browse/games/release-date/available/xboxone/date',
        'https://www.metacritic.com/browse/games/release-date/available/xbox-series-x/date',
        'https://www.metacritic.com/browse/games/release-date/available/n64/date',
        'https://www.metacritic.com/browse/games/release-date/available/wii/date',
        'https://www.metacritic.com/browse/games/release-date/available/wii-u/date',
        'https://www.metacritic.com/browse/games/release-date/available/gamecube/date',
        'https://www.metacritic.com/browse/games/release-date/available/gba/date',
        'https://www.metacritic.com/browse/games/release-date/available/3ds/date',
        'https://www.metacritic.com/browse/games/release-date/available/switch/date',
        'https://www.metacritic.com/browse/games/release-date/available/dreamcast/date',
        'https://www.metacritic.com/browse/games/release-date/available/pc/date'
        ]

    #first details page function to crawl to the videogame webpage
    def parse(self, response):
        urls = response.css('tr > td > a::attr(href)').extract()
        for link in urls:
            yield scrapy.Request(url= 'https://www.metacritic.com' + link, callback=self.parse_details_credits_link)

        #pagination funtion for the videogame listing
        next_page = response.xpath("//a[@rel='next']/@href").extract_first()
        if next_page:
            yield scrapy.Request(url='https://www.metacritic.com' + next_page,callback=self.parse)


    #second detailspage function for the spider to crawl to the details and credits information page
    def parse_details_credits_link(self, response):
        detailslink = response.css('ul > li.nav.nav_details > span > span >a::attr(href)').get()

        if detailslink:
           yield scrapy.Request(url='https://www.metacritic.com' + detailslink, callback=self.parse_details)


    #yield function to store the specified data within a dictionary "data"
    def parse_details(self, response):
        Game = response.css('div.product_title > a > h1::text').get()
        Metascore = response.css('div > a > div > span::text').get()
        UserScore = response.css('div > div > a > div.metascore_w.user.large.game.mixed::text').get()
        Publisher = str(response.css('div.product_data > ul > li.summary_detail.publisher > span.data > a::text').get()).strip()
        ReleaseDate = response.css('div.product_data > ul > li.summary_detail.release_data > span.data::text').get()
        Genre = str(response.css('tr:nth-child(3) > td::text').get()).strip().replace(' ','')
        NumberOfOnlinePlayers = str(response.css('tr:nth-child(4) > td::text').get()).strip().replace(' ','')
        Cast = str(response.css('tbody > tr > td.person > a::text').getall()).strip().replace(' ','').replace('[','').replace(']','').replace('\\\n','').replace("\\n","").replace("\'"," ")
        Credits = str(response.css('tbody > tr > td.role::text').getall()).strip().replace(' ','').replace('[','').replace(']','').replace('\\\n','').replace("\\n","").replace("\'"," ")


        data = {
            'Game': Game,
            'Metascore': Metascore,
            'UserScore': UserScore,
            'Publisher': Publisher,
            'ReleaseDate': ReleaseDate,
            'Genre': Genre,
            'NumberOfOnlinePlayers': NumberOfOnlinePlayers,
            'Cast': Cast,
            'Credits': Credits
            }


        criticslink = 'https://www.metacritic.com' + response.css('li.nav.nav_critic_reviews > span > span > a::attr(href)').get()
        if criticslink:
           yield scrapy.Request(url=criticslink, callback=self.parse_critics_details, meta={'data': data})


    #next fetch function to parse the webpage content of the critic details and review text and store it within the "reviews_obj" list
    def parse_critics_details(self, response):
        data = response.meta['data']

        reviews_obj = []
        reviews = response.xpath('//ol[@class="reviews critic_reviews"]/li[contains(@class, "review critic_review")]')

        for critics in reviews:
            reviews_obj.append(
                {
                'CriticName': critics.css('div.review_stats > div.review_critic > div.source::text').get(),
                'CriticScore' : critics.css('div.review_stats > div.review_grade > div::text').get(),
                'CriticReviewDate' : critics.css('div.review_stats > div.review_critic > div.date::text').get(),
                'CriticReviewText' : str(critics.css('div > div:nth-child(1) > div.review_body::text').get()).strip().replace('\n','')
                }
            )

        data.update({
            'CriticsReviews': reviews_obj,
        })

        next_page = response.xpath("//a[@rel='next']/@href").extract_first()
        if next_page:
            yield scrapy.Request(url='https://www.metacritic.com' + next_page,callback=self.parse_critics_details)
        else:
            userlink = response.xpath("//ul[@class='nav_items content_nav']//a[contains(text(),'User Reviews')]/@href").extract_first()
            if userlink:
               yield scrapy.Request(url= 'https://www.metacritic.com' + userlink, callback=self.parse_user_details, meta={'data': data})


    #last fetch function to parse the webpage content of the user details and review text and store it within the "reviews_obj" list
    def parse_user_details(self, response):
        data = response.meta['data']

        reviews_obj = []
        reviews = response.xpath('//ol[@class="reviews user_reviews"]/li[contains(@class, "review user_review")]')

        for UserReviews in reviews:
            reviews_obj.append(
                {
                'UserName': UserReviews.css('div.review_stats > div.review_critic > div.name > a::text').get(),
                'UserReviewScore' : UserReviews.css('div.review_stats > div.review_grade > div::text').get(),
                'UserReviewDate' : UserReviews.css('div.review_stats > div.review_critic > div.date::text').get(),
                'UserReviewText' : str(response.css('div > div.review_body > span::text').get()).strip().replace("\r","").replace("\\r","").replace('[','').replace(']','').replace(' \ ','').replace("\'"," ").replace('    ,','').replace('   ,',''),
                'ExpandedUserReviewText': str(response.css('#review_blurb_8765866 > span.blurb.blurb_expanded::text').get()).strip().replace("\r","").replace("\\r","").replace('[','').replace(']','').replace(' \ ','').replace("\'"," "),
                'TotalThumbsUp': str(response.css('div.helpful_summary.thumb_count > a > span.total_ups::text').get()),
                'TotalThumbs': str(response.css('div.helpful_summary.thumb_count > a > span.total_thumbs::text').get())
                }
            )

        data.update({
            'UserReviews': reviews_obj,
        })

        yield data

        next_page = response.xpath("//a[@rel='next']/@href").extract_first()
        if next_page:
            yield scrapy.Request(url='https://www.metacritic.com' + next_page,callback=self.parse_user_details)