from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('profile/', include("backend.profiles.urls")),
    path('search/', include("backend.search.urls")),
    path('', include("backend.callboard.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)