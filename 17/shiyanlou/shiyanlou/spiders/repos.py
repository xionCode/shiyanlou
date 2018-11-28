# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import RepoItem


class ReposSpider(scrapy.Spider):
    name = 'repos'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        next_page_url = response.xpath('//a[contains(text(), "Next")]/@href').extract_first()
        for repository in response.css('li.public'):
            item = RepoItem()
            item['name'] = repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)')
            item['update_time'] = repository.xpath('.//relative-time/@datetime').extract_first()
            repo_url = response.urljoin(repository.xpath('.//a[@itemprop="name codeRepository"]/@href').extract_first())
            request = scrapy.Request(repo_url, callback=self.parse_repo)
            request.meta['item'] = item
            yield request

        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_repo(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('(//span[@class="num text-emphasized"])[1]/text()').re_first('[^\d]*(\d+)[^\d]*')
        item['branches'] = response.xpath('(//span[@class="num text-emphasized"])[2]/text()').re_first('[^\d]*(\d+)[^\d]*')
        item['releases'] = response.xpath('(//span[@class="num text-emphasized"])[3]/text()').re_first('[^\d]*(\d+)[^\d]*')
        yield item

