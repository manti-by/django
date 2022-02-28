from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.shop.serializers import (
    PurchaseCreateSerializer,
    ProductModelSerializer,
    ProductFiltersSerializer,
)
from shop.models import Product, Purchase
from shop.queries import filter_products


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """

    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        serializer = ProductFiltersSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        cost__gt = serializer.validated_data.get("cost__gt")
        cost__lt = serializer.validated_data.get("cost__lt")
        order_by = serializer.validated_data.get("order_by")

        return filter_products(queryset, cost__gt, cost__lt, order_by)


class PurchaseCreateView(CreateAPIView):
    """
    API endpoint that allows to create users.
    """

    serializer_class = PurchaseCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get("product_id")
        if not product_id:
            raise NotFound
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound
        serializer = self.get_serializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        Purchase.objects.create(
            user=request.user, product=product, count=serializer.validated_data["count"]
        )
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        raise PermissionDenied
