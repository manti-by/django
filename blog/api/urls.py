from django.urls import include, path
from rest_framework import routers
from api.views import PostViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
