# -*- coding: utf-8 -*-
import scrapy
from PCofficeroom.items import PcofficeroomItem
import logging
import urllib.request
import re, time, random
from scrapy.http import Request

#运行爬虫命令
logger = logging.getLogger('mycustomlogger')

class OfficeSpider(scrapy.Spider):
    name = "office"
    allowed_domains = ["sz.kfang.com"]
    start_urls = [
        'https://sz.kfang.com/office/rent/page1',
    ]

    # 回调函数
    def parse(self, response):
        init_url = "https://sz.kfang.com/office/rent/page"

        sels = response.xpath('//div[@class="list-item clearfix"]')
        # print(sels)
        roomid_list = response.xpath('//div[@class="list-item clearfix"]/div/p/a/@href').extract()
        roomtitle_list = sels.xpath('//div/div/p/a/@title').extract()
        i = 0
        for sel in sels:
            item = PcofficeroomItem()
            item["roomid"] = roomid_list[i].strip()
            item['roomtile'] = roomtitle_list[i].strip()
            i += 1
            # yield item
            yield scrapy.Request(
                "https://sz.kfang.com"+item["roomid"],
                callback=self.parse_detail,
                meta={"item":item}
            )
            print(item["roomid"]+"  "+item["roomtile"])

        print(response)
        #当前页码
        page_num = response.xpath(
            '//div[@class="fr"]/ul/li[@class="ivu-page-item ivu-page-item-active"]/a/text()'
        ).extract()
        print("获取到的当前页码：{}".format(page_num))
        page_result = int(page_num[0])
        print(page_result)

        if page_result < 804:
            nex_page = int(page_result) + 1
            url = ''.join([init_url, str(nex_page), '/'])
            print('starting scrapy url:',url)
            time.sleep(round(random.uniform(1, 2), 2))
            yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        roomid_detail = response.xpath(
            "//*[@id=\"__layout\"]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[3]/text()").extract()
        for i in roomid_detail:
            if i == None:
                item["roomno"] = "null"
                print("获取空的详详情编码".format(item["roomno"]))
            else:
                item["roomno"] = i
        yield item
        # yield scrapy.Request(url= init_url,callback=self.parse, dont_filter=False)
        # f = open("data.txt", "w")

