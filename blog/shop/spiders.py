import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            data = {
               "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
               "cost": product.css(".product-price-block .price__normal::text").get().strip(),
               "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
            }
            yield data
