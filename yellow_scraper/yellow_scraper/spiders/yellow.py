import scrapy
from ..items import YellowScraperItem


class YellowSpider(scrapy.Spider):
    name = 'yellow'
    next_page_no = 2
    start_urls = [
        'https://www.yellowpages.com/coloma-mi/restaurants'
    ]

    def parse(self, response):
        items = YellowScraperItem()
        all_data = response.css('div.result')

        for data in all_data:
            name = data.css('a.business-name').css('::text').extract()
            # reviews = response.css('').css('').extract()
            rating = data.css('div.ratings').css('::attr(data-tripadvisor)').extract()
            phone = data.css('div.phones.phone.primary').css('::text').extract()
            street_address = data.css('div.street-address').css('::text').extract()
            locality = data.css('div.locality').css('::text').extract()
            website = data.css('a.track-visit-website').css('::attr(href)').extract()

            items['name'] = name
            # items['reviews'] = reviews
            items['rating'] = rating
            items['phone'] = phone
            items['street_address'] = street_address
            items['locality'] = locality
            items['website'] = website

            yield items

            next_page = 'https://www.yellowpages.com/coloma-mi/restaurants?page=' + str(YellowSpider.next_page_no)

            if YellowSpider.next_page_no <= 13:
                YellowSpider.next_page_no += 1
                yield response.follow(next_page, callback=self.parse)
