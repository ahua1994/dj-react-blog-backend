from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"
