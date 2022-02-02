from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.profiles.views import ProfileViewSet
from api.users.views import UserViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"users", UserViewSet, basename="users")
router.register(r"profiles", ProfileViewSet, basename="profiles")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
