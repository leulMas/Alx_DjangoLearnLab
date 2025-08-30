from rest_framework.decorators import action
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .models import Post
from .serializers import PostListSerializer
from rest_framework.pagination import PageNumberPagination

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        target = self.get_object()
        if request.user == target:
            return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."})

    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        target = self.get_object()
        request.user.following.remove(target)
        return Response({"detail": f"You have unfollowed {target.username}."})
        
class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def list(self, request):
        user = request.user
        posts = Post.objects.filter(author__in=user.following.all()).order_by("-created_at")
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(posts, request)
        serializer = PostListSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
