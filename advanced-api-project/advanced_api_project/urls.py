# advanced_api_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from api.views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', lambda request: redirect('/api/')),  # root → /api/
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
