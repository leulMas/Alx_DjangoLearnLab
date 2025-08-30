from django.urls import path
from .views import RegisterView, ProfileView, FollowView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<str:username>/", FollowView.as_view(), name="follow"),
    path("", include(router.urls)),
    path("follow/<int:user_id>/", views.follow_user, name="follow-user"),
    path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow-user"),
]

# --- JWT login endpoints (SimpleJWT) ---
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns += [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

