from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment

User = get_user_model()


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "author", "created_at", "updated_at", "comments_count"]


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at", "updated_at", "comments"]

    def get_comments(self, obj):
        # return minimal comment info for embed — careful with large payloads
        return [
            {"id": c.id, "author": c.author.username, "content": c.content, "created_at": c.created_at}
            for c in obj.comments.all().order_by("created_at")
        ]


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    post_id = serializers.PrimaryKeyRelatedField(source="post", queryset=Post.objects.all(), write_only=True)
    post = serializers.ReadOnlyField(source="post.id")

    class Meta:
        model = Comment
        fields = ["id", "post", "post_id", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "post", "created_at", "updated_at"]

    def create(self, validated_data):
        # `post` comes from post_id mapped to source "post"
        return super().create(validated_data)

