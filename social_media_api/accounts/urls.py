from django.urls import path
from .views import RegisterView, ProfileView, FollowView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<str:username>/", FollowView.as_view(), name="follow"),
    path("", include(router.urls)),
]

# --- JWT login endpoints (SimpleJWT) ---
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns += [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# --- If you choose DRF TokenAuthentication instead, comment the JWT lines above
# and add the DRF token obtain endpoint below:
# from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns += [
#     path("login/", obtain_auth_token, name="token_login"),
# ]

