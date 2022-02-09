import logging

from django.core.management.base import BaseCommand

from shop.models import Product
from shop.spiders import OmaSpider
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):

        def crawler_results(signal, sender, item, response, spider):
            item["cost"] = int(item["cost"].split(",")[0])
            Product.objects.get_or_create(external_id=item["external_id"], defaults=item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()
