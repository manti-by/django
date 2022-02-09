from django.conf import settings
from django.db import models

STATUS_CHOICES = (("IN_STOCK", "In Stock"), ("OUT_OF_STOCK", "Out Of Stock"))

ORDER_BY_CHOICES = (
    ("cost_asc", "Cost Asc"),
    ("cost_desc", "Cost Desc"),
    ("max_count", "Max Count"),
    ("max_price", "Max Cost"),
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    cost = models.IntegerField()
    external_id = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="IN_STOCK"
    )

    def __str__(self):
        return f"{self.title} - {self.cost}"


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.count}"
