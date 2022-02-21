from django.core.management.base import BaseCommand

from shop.tasks import run_products_update


class Command(BaseCommand):
    help = "Run worker"

    def handle(self, *args, **options):
        run_products_update.delay()
