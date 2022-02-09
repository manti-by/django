import logging

from django.db.models import Sum, F
from django.shortcuts import render, get_object_or_404

from shop.forms import ProductFiltersForm
from shop.models import Product

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    filters_form = ProductFiltersForm(request.GET)

    if filters_form.is_valid():
        price__gt = filters_form.cleaned_data["price__gt"]
        if price__gt:
            products = products.filter(cost__gt=price__gt)

        price__lt = filters_form.cleaned_data["price__lt"]
        if price__lt:
            products = products.filter(cost__lt=price__lt)

        order_by = filters_form.cleaned_data["order_by"]
        if order_by:
            if order_by == "price_asc":
                products = products.order_by("cost")
            if order_by == "price_desc":
                products = products.order_by("-cost")
            if order_by == "max_count":
                products = products.annotate(total_count=Sum("purchases__count")).order_by(
                    "-total_count"
                )
            if order_by == "max_price":
                products = products.annotate(
                    total_price=Sum("purchases__count") * F("price")
                ).order_by("-total_price")

    return render(request, "products/list.html", {"filters_form": filters_form, "products": products})


def product_details_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/details.html", {"product": product})
