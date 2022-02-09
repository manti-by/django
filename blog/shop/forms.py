from django import forms
from django.core.exceptions import ValidationError

from shop.models import ORDER_BY_CHOICES


class ProductFiltersForm(forms.Form):
    price__gt = forms.IntegerField(
        min_value=0,
        label="Price Min",
        widget=forms.TextInput(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
    price__lt = forms.IntegerField(
        min_value=0,
        label="Price Max",
        widget=forms.TextInput(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
    order_by = forms.ChoiceField(
        choices=ORDER_BY_CHOICES,
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        price__gt = cleaned_data.get("price__gt")
        price__lt = cleaned_data.get("price__lt")
        if price__gt and price__lt and price__gt > price__lt:
            raise ValidationError("Min price can't be greater than Max price")


class PurchasesFiltersForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ("-created_at", "Newest First"),
            ("created_at", "Oldest First"),
        ),
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
