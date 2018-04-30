# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import YiwushibaqiangItem
import re


class GetitSpider(scrapy.Spider):
    name = 'getit'
    allowed_domains = ['18qiang.com']
    start_urls = ['http://www.18qiang.com/read-htm-tid-523576-page-1.html']

    pattern = re.compile(".*\(.*\)\xa0")

    def parse(self, response):
        read_t = response.css("div.read_t")
        shibaqiang = YiwushibaqiangItem()
        for p in read_t:
            readName = p.css("div.readName.b a::text").extract_first()
            shibaqiang["review"] = readName
            problemAndproblem_who = p.css("div.text::text").extract()
            if problemAndproblem_who:
                 shibaqiang["problem"] = problemAndproblem_who[1]
                 shibaqiang["problem_who"] = problemAndproblem_who[0]
                 shibaqiang["problem_time"] = p.xpath(".//div[@class='text']/span[2]/text()").re_first("\((.*)\)")
            comment = p.xpath("string(.//div[@class='khd_m fs16'])").extract_first()
            shibaqiang["comment"] = self.pattern .sub(' ', comment)
            print(shibaqiang)
            yield shibaqiang

        #next_url = response.css("div.cc div.pages a.pages_next::attr(href)").extract_first()
        le = LinkExtractor(restrict_css='div.cc div.pages a.pages_next')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)
