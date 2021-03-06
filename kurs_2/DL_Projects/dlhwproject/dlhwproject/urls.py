from django.conf.urls import url
from django.contrib.staticfiles.urls import static

from . import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include('advito.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)

