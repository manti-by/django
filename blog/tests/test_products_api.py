import pytest

from django.contrib.auth.models import User

from django.test import Client

from shop.models import Product


@pytest.mark.django_db
class TestProductsApi:
    def test_products_api(self):
        client = Client()

        user = User.objects.create(
            username="test", email="test@test.com", password="test"
        )
        Product.objects.create(title="Test", cost=100)

        client.force_login(user)

        response = client.get("/api/products/")
        assert response.status_code == 200
        assert response.data["results"][0]["title"] == "Test"
