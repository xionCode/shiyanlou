import scrapy

class ShiyanlouRepoSpider(scrapy.Spider):
	name = 'shiyanlou-repo'

	@property 
	def start_urls(self):
		return ('https://github.com/shiyanlou?tab=repositories',
			'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxMFrOBZKVZw%3D%3D&tab=repositories',
			'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwMzozMDoyNVrOAcdiUA%3D%3D&tab=repositories',
			'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNC0xMS0yMVQxMDowOTowMlrOAZ0AWQ%3D%3D&tab=repositories')

	def parse(self, response):
		for repository in response.css('li.public'):
			yield {
				'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
				'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
			}