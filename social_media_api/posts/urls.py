from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedViewSet


router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"feed/", FeedViewSet, basename="feed/") 


urlpatterns = [
    path("", include(router.urls)),
]

