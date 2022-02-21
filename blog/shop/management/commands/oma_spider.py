import logging

from django.core.management.base import BaseCommand

from shop.tasks import run_oma_spider

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        run_oma_spider.delay()
