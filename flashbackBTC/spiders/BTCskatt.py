# -*- coding: utf-8 -*-
import scrapy


class BtcskattSpider(scrapy.Spider):
    name = 'BTCskatt'
#    allowed_domains = ['https://www.flashback.org/']
    start_urls = ['https://www.flashback.org/t2680579/']

    def parse(self, response):
        timeDate = response.xpath('.//*/div[@class="post-heading"]/text()').extract()
        userName = response.xpath('.//*[@class="post-user-username dropdown-toggle"]/text()').extract()
        profileUrls = response.xpath('.//*[@class="post-user-username dropdown-toggle"]/@href').extract()
        postMsg = response.xpath('.//*/div[@class="post_message"]/text()').extract()


        yield{'TimeDate': timeDate,
              'UserName': userName,
              'ProfileUrls': profileUrls,
              'PostMsg': postMsg}

        next_page_url = response.xpath('.//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)

        yield scrapy.Request(absolute_next_page_url)
