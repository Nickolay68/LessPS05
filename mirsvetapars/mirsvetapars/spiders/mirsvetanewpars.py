import scrapy


class MirsvetanewparsSpider(scrapy.Spider):
    name = "mirsvetanewpars"
    allowed_domains = ["https://mirsveta.by"]
    start_urls = ["https://mirsveta.by/katalog/"]

    def parse(self, response):
        mirsveta = response.css("div._cont-fluid")
        for mirsveta in mirsvetas:
            yield {'name' : mirsveta.css('div.container::text').get()
                   'price' :mirsveta.css('div.itemListElement::text').get()
            }


