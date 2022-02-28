from rest_framework import serializers

from shop.models import Product


class PurchaseCreateSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=1)


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "cost", "external_id", "description", "image", "link", "status"]
