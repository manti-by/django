import logging

import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c?PAGEN_1=2"]

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("scrapy")
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            image_link = product.css('.product-item_img-box img:first-child::attr(data-lazy)').get()
            data = {
                "external_id": int(product.css("::attr(data-ga-product-id)").get()),
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": product.css(".product-price-block .price__normal::text").get().strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                "image": f"{self.allowed_domains[0]}{image_link}",
            }
            yield data
