from django.contrib import admin
from django.urls import path
from accounts.views import home  # Import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL points to home view
]

# If you serve media files in dev, keep this:
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
