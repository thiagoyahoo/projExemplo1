import scrapy

class MainSpider(scrapy.Spider):
    name = 'main_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
#        self.log('Estou aqui {}'.format(response.url))

        texts1 = response.xpath('//span[@class="text"]/text()').extract()
        for text1 in texts1:
            yield {
                'text': text1
            }

        texts2 = response.xpath('//small[@class="author"]/text()').extract()
        for text2 in texts2:
            yield {
                'text': text2
            }