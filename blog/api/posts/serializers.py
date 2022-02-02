from rest_framework import serializers

from posts.models import Post


class PostModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "image", "text", "created_at"]
