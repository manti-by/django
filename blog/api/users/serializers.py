from django.contrib.auth.models import User
from rest_framework import serializers


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "date_joined",
        )
        read_only_fields = ("id", "date_joined")


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=256, write_only=True)
