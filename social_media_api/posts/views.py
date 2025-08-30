from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
    CommentSerializer,
)
from .permissions import IsOwnerOrReadOnly


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author").prefetch_related("comments").all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = []  # if you want to filter by exact fields like author id: ["author"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]

    def get_serializer_class(self):
        if self.action in ["list"]:
            return PostListSerializer
        if self.action in ["retrieve"]:
            return PostDetailSerializer
        if self.action in ["create", "update", "partial_update"]:
            return PostCreateUpdateSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("author", "post").all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["content", "author__username"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        # Set author automatically from request
        serializer.save(author=self.request.user)
