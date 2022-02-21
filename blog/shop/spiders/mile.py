import logging

import scrapy


class MileSpider(scrapy.Spider):
    name = "mile.by"
    allowed_domains = ["mile.by"]
    start_urls = ["https://mile.by/catalog/elektroinstrument/"]

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("scrapy")
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        for product in response.css(".showcase-sorting-block .anons-wrap"):
            image_link = product.css(".anons-foto img::attr(src)").get()
            price = product.css(".anons-price-wrap .price span::text").get()
            price = price.strip().split(".")[0] if price is not None else 0
            data = {
                "external_id": int(
                    product.css(".anons-sku::text").get().replace("Арт. ", "")
                ),
                "title": product.css(".anons-name a::text").get().strip(),
                "cost": int(price),
                "link": f'https://{self.allowed_domains[0]}{product.css(".anons-name a::attr(href)").get()}',
                "image": f"https://{self.allowed_domains[0]}{image_link}",
                "status": "IN_STOCK" if price else "OUT_OF_STOCK",
            }
            yield data

        next_page = response.css(
            ".pagination-wrap .pagin-arrow:last-child::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
