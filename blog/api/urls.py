from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.profiles.views import ProfileViewSet
from api.shop.views import PurchaseCreateView, ProductViewSet
from api.users.views import UserViewSet, UserCreateView, UserLoginView, UserLogoutView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"users", UserViewSet, basename="users")
router.register(r"profiles", ProfileViewSet, basename="profiles")


urlpatterns = [
    path("", include(router.urls)),
    path("products/<int:product_id>/", PurchaseCreateView.as_view(), name="purchase"),
    path("products/", ProductViewSet.as_view(), name="products"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
