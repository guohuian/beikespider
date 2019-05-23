# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from .citys import CitysSpider

class MybeikeSpider(CrawlSpider):
    name = 'mybeike'
    allowed_domains = ['ke.com']
    start_urls = ['https://sz.ke.com/ershoufang/']

    rules = [
       Rule(
           # LinkExtractor(allow=('/ershoufang/pg\d+'),
           LinkExtractor(restrict_xpaths=('//*[@class="contentBottom clear"]'),
             ),
           callback="parse_housing_url",
           follow=True,
       )
    ]

    # def parse_item(self, response):
    #     nav_list = response.xpath('//*[@class="nav typeUserInfo"]/ul/li')[:1]
    #     for navs in nav_list:
    #         nav_url = navs.xpath('./a/@href').get()
    #         request = scrapy.Request(url=nav_url, callback=self.parse_housing_url)
    #         yield request

    def parse_housing_url(self, response):
        position_list = response.xpath('//*[@class="position"]/dl[2]/dd/div/div/a')
        for positions in position_list:
            position = positions.xpath('./text()').get()
            urls ="https://sz.ke.com" +  positions.xpath('./@href').get()
            requests = scrapy.Request(url=urls, callback=self.get_housing)
            yield requests

    def get_housing(self, response):
        housing_list = re.findall('<li class="clear">.*?</li>', response.text, re.S)
        for housing in housing_list:
            title = re.findall('<a.*?>(.*?)</a>', housing, re.S)[1]
            address = re.findall('<a.*?>(.*?)</a>', housing, re.S)[2]
            house_icon = re.findall('<span class="houseIcon"></span>(.*?)</div>', housing, re.S)[0]
            star_icon = re.findall('<span class="starIcon"></span>(.*?)</div>', housing, re.S)[0].strip()
            total_price = re.findall('<div class="totalPrice"><span>(.*?)</span>(.*?)</div>',  housing, re.S)[0]
            unit_price = re.findall('<span>(.*?)</span>', housing, re.S)[1]
            urls = re.findall('<a class="img.*?" href="(.*?)"', housing, re.S)[0]
            request2 = scrapy.Request(url=urls, callback=self.get_detail)
            yield request2

    def get_detail(self, response):
        base_list = response.xpath('//*[@class="base"]/div[@class="content"]/ul')
        record_label = response.xpath('//*[@class="houseRecord"]/span[1]/text()').get()
        record_info = response.xpath('//*[@class="houseRecord"]/span[2]/text()').get()
        broker_name = response.xpath('//*[@class="brokerName"]/a/text()').get()
        broker_phone = response.xpath('//*[@class="phone"]/div/text()').get()
        for bases in base_list:
            type_label = bases.xpath('./li[1]/span/text()').get()
            house_type = bases.xpath('./li[1]/text()').get()
            floor_label = bases.xpath('./li[2]/span/text()').get()
            house_floor = bases.xpath('./li[2]/text()').get()
            floorage_label = bases.xpath('./li[3]/span/text()').get()
            house_floorage = bases.xpath('./li[3]/text()').get()
            structure_label = bases.xpath('./li[4]/span/text()').get()
            house_structure = bases.xpath('./li[4]/text()').get()
            area_label = bases.xpath('./li[5]/span/text()').get()
            house_area = bases.xpath('./li[5]/text()').get()
            building_label = bases.xpath('./li[6]/span/text()').get()
            house_building = bases.xpath('./li[6]/text()').get()
            struc_label = bases.xpath('./li[7]/span/text()').get()
            house_struc = bases.xpath('./li[7]/text()').get()
            renovation_label = bases.xpath('./li[8]/span/text()').get()
            house_renovation = bases.xpath('./li[8]/text()').get()
            trim_label = bases.xpath('./li[9]/span/text()').get()
            house_trim = bases.xpath('./li[9]/text()').get()
            Ladder_label = bases.xpath('./li[10]/span/text()').get()
            house_Ladder = bases.xpath('./li[10]/text()').get()
            elevator_label = bases.xpath('./li[11]/span/text()').get()
            house_elevator = bases.xpath('./li[11]/text()').get()
            property_label = bases.xpath('./li[12]/span/text()').get()
            house_property = bases.xpath('./li[12]/text()').get()

        transaction_list = response.xpath('//*[@class="transaction"]/div[@class="content"]/ul')
        for transactions in transaction_list:
            listed_label = transactions.xpath('./li[1]/span/text()').get()
            listed_time = transactions.xpath('./li[1]/text()').get()
            ownership_label = transactions.xpath('./li[2]/span/text()').get()
            house_ownership = transactions.xpath('./li[2]/text()').get()
            deal_label = transactions.xpath('./li[3]/span/text()').get()
            house_deal = transactions.xpath('./li[3]/text()').get()
            purpose_label = transactions.xpath('./li[4]/span/text()').get()
            house_purpose = transactions.xpath('./li[4]/text()').get()
            year_label = transactions.xpath('./li[5]/span/text()').get()
            house_year = transactions.xpath('./li[5]/text()').get()
            authority_label = transactions.xpath('./li[6]/span/text()').get()
            house_authority = transactions.xpath('./li[6]/text()').get()
            mortgage_label = transactions.xpath('./li[7]/span/text()').get()
            house_mortgage = transactions.xpath('./li[7]/text()').get()
            premises_label = transactions.xpath('./li[8]/span/text()').get()
            house_premises = transactions.xpath('./li[8]/text()').get()
            code_label = transactions.xpath('./li[9]/span/text()').get()
            house_code = transactions.xpath('./li[9]/text()').get()

        apartment_list = response.xpath('//*[@id="infoList"]/div')
        for apartments in apartment_list:
            room_type = apartments.xpath('./div[1]/text()').get()
            room_area = apartments.xpath('./div[2]/text()').get()
            room_orientation = apartments.xpath('./div[3]/text()').get()
            room_window = apartments.xpath('./div[4]/text()').get()
            print(room_type)


