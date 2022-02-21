from rest_framework import serializers

from profiles.models import Profile


class ProfileModelSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name="api:users-detail", read_only=True
    )

    class Meta:
        model = Profile
        fields = ["id", "user", "age", "created_at"]
        read_only_fields = ["id", "user", "created_at"]
