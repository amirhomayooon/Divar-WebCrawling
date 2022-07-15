import scrapy
from decouple import config
url = 'https://divar.ir/v/-/{token}'

token_file = open(
    config('file'), "r", encoding="utf8"
)
tokens = token_file.read().split('.')
token_file.close()


class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [url.format(token=token) for token in tokens]

    def parse(self, response):
        info = response.css('div span.kt-group-row-item__value::text')
        area = int(info[0].extract())

        price = response.css(
            'div p.kt-unexpandable-row__value::text').extract_first()

        yield {
            'area': area,
            'price': price,
        }
