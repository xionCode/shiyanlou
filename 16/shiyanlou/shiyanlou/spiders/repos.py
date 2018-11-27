# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepoItem


class ReposSpider(scrapy.Spider):
    name = 'repos'
    start_urls = ['']

    @property 
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxMFrOBZKVZw%3D%3D&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwMzozMDoyNVrOAcdiUA%3D%3D&tab=repositories',
            'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNC0xMS0yMVQxMDowOTowMlrOAZ0AWQ%3D%3D&tab=repositories')

    def parse(self, response):
        for repository in response.css('li.public'):
            yield RepoItem({
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
            })

