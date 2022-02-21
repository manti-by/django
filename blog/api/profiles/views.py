from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from api.profiles.serializers import ProfileModelSerializer
from profiles.models import Profile


class ProfileViewSet(
    ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    """
    API endpoint that allows get or update users profile.
    """

    queryset = Profile.objects.all().order_by("-created_at")
    serializer_class = ProfileModelSerializer
    permission_classes = [IsAuthenticated]
