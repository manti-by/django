import logging

import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("scrapy")
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            image_link = product.css('.product-item_img-box img:first-child::attr(data-lazy)').get()
            if not image_link:
                image_link = product.css(".product-item_img-box img:first-child::attr(data-src)").get()
            price = product.css(".product-price-block .price__normal::text").get()
            price = price.strip() if price is not None else 0
            data = {
                "external_id": int(product.css("::attr(data-ga-product-id)").get()),
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": price,
                "link": f"https://{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                "image": f"https://{self.allowed_domains[0]}{image_link}",
                "status": "IN_STOCK" if price else "OUT_OF_STOCK",
            }
            yield data

        next_page = response.css(".page-nav_box .btn__nav-right::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
