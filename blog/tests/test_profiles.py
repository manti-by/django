from django.test import Client


class TestProfiles:
    def test_profiles_index_view(self):
        client = Client()

        response = client.get("/profiles/")
        assert response.status_code == 200

        response = client.get("/profiles/?get-key-1=test-key-1")
        assert response.status_code == 200

        response = client.get(
            "/profiles/?get-key-1=test-key-1&get-key-2=test-key-2&get-key-3=test-key-3"
        )
        assert response.status_code == 200

        response = client.post(
            "/profiles/?get-key-1=test-key-1", data={"post-key-2": "test-key-2"}
        )
        assert response.status_code == 200

        response = client.post(
            "/profiles/", data={"post-key-1": "test-key-1", "post-key-3": "test-key-2"}
        )
        assert response.status_code == 200
