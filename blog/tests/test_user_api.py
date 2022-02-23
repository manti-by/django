import pytest

from faker import Faker
from django.contrib.auth.models import User
from django.test import Client

faker = Faker()


@pytest.mark.django_db
class TestUserApi:
    def test_register_api(self):
        client = Client()

        data = {
            "email": faker.email(),
            "password": faker.password(),
        }
        response = client.post("/api/register/", data=data)
        assert response.status_code == 201
        assert User.objects.exists()
