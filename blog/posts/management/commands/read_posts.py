import logging

import csv

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from posts.models import Post

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Print posts"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                user, _ = User.objects.get_or_create(username=row[0])
                Post.objects.create(author=user, title=row[1], slug=row[2], text=row[3])
