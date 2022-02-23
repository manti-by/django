from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.users.serializers import UserModelSerializer, UserCreateSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    API endpoint that allows get user.
    """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    """
    API endpoint that allows to create users.
    """

    serializer_class = UserCreateSerializer
    permission_classes = []

    def perform_create(self, serializer):
        user = User(
            username=serializer.validated_data["email"],
            email=serializer.validated_data["email"],
        )
        user.set_password(serializer.validated_data["password"])
        user.save()
