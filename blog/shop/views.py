import logging

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from shop.forms import ProductFiltersForm
from shop.models import Product, Purchase
from shop.queries import filter_products

logger = logging.getLogger(__name__)


class ProductListView(TemplateView):
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.all().order_by("id")
        filters_form = ProductFiltersForm(self.request.GET)

        if filters_form.is_valid():
            cost__gt = filters_form.cleaned_data["cost__gt"]
            cost__lt = filters_form.cleaned_data["cost__lt"]
            order_by = filters_form.cleaned_data["order_by"]

            products = filter_products(products, cost__gt, cost__lt, order_by)

        paginator = Paginator(products, 30)
        page_number = self.request.GET.get("page")
        products = paginator.get_page(page_number)

        return {"products": products, "filters_form": filters_form}


def product_details_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        if request.POST.get("count"):
            Purchase.objects.create(
                product=product, user=request.user, count=request.POST.get("count")
            )
            return redirect("product_details_view", product_id=product_id)
    return render(request, "products/details.html", {"product": product})
