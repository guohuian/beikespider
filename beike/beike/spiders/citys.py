# -*- coding: utf-8 -*-
import scrapy

class CitysSpider(scrapy.Spider):
    name = 'citys'
    allowed_domains = ['ke.com']
    start_urls = ['https://www.ke.com/city/']

    def parse(self, response):
        city_list = response.xpath('//*[@class="city_recommend"]/div[1]/div[2]/ul/li')
        for citys in city_list:
            city_letter = citys.xpath('./div[1]/span/text()').get()
            city_tit = citys.xpath('./div[2]/div/div/text()').get().strip()
            city_province = citys.xpath('./div[2]/div/ul/li')
            for cityss in city_province:
                city_name = cityss.xpath('./a/text()').get()
                urls = "https:" + cityss.xpath('./a/@href').get()
                requests = scrapy.Request(url=urls, callback=self.get_housing)
                yield requests

    def get_housing(self, response):
        response.xpath('//*[@class="nav typeUserInfo"]/ul/li')

