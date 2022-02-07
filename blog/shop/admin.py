from django.contrib import admin

from shop.models import Product, Purchase


class PurchaseInline(admin.TabularInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "cost"]
    search_fields = ["title"]
    inlines = [
       PurchaseInline,
    ]
