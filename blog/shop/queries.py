from django.db.models import Sum, F


def filter_products(products, cost__gt, cost__lt, order_by):
    if cost__gt is not None:
        products = products.filter(cost__gt=cost__gt)
    if cost__lt is not None:
        products = products.filter(cost__lt=cost__lt)
    if order_by:
        if order_by == "cost_asc":
            products = products.order_by("cost")
        if order_by == "cost_desc":
            products = products.order_by("-cost")
        if order_by == "max_count":
            products = products.annotate(total_count=Sum("purchases__count")).order_by(
                "-total_count"
            )
        if order_by == "max_price":
            products = products.annotate(
                total_cost=Sum("purchases__count") * F("cost")
            ).order_by("-total_cost")
    return products
