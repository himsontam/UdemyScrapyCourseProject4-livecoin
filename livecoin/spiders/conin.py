# -*- coding: utf-8 -*-
import scrapy


class ConinSpider(scrapy.Spider):
    name = 'conin'
    allowed_domains = ['www.liveconin.net']
    start_urls = ['http://www.liveconin.net/']

    def parse(self, response):
        pass
