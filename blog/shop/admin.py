from django.contrib import admin

from shop.models import Product, Purchase


class PurchaseInline(admin.TabularInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "external_id", "cost", "status"]
    search_fields = ["title"]
    inlines = [
        PurchaseInline,
    ]
    list_filter = ["status"]
