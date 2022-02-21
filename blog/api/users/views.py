from django.contrib.auth.models import User
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.users.serializers import UserModelSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    API endpoint that allows get user.
    """

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
