import pytest

from django.contrib.auth.models import User

from django.test import Client

from posts.models import Post


@pytest.mark.django_db
class TestPostsApi:
    def test_profiles_index_view(self):
        client = Client()

        user = User.objects.create(
            username="test", email="test@test.com", password="test"
        )
        Post.objects.create(author=user, title="Test", text="test")

        client.force_login(user)

        response = client.get("/api/posts/")
        assert response.status_code == 200
        assert response.data[0]["title"] == "Test"

        response = client.post("/api/posts/", data={"title": "Test", "text": "test"})
        assert response.status_code == 201
