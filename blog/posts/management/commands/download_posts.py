import csv

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = "Download CSV and create posts"

    def handle(self, *args, **options):
        r = requests.get("https://content.manti.by/posts.csv")
        open(settings.BASE_DIR / "posts.csv", "wb").write(r.content)
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                user, _ = User.objects.get_or_create(username=row[0])
                Post.objects.create(author=user, title=row[1], slug=row[2], text=row[3])
