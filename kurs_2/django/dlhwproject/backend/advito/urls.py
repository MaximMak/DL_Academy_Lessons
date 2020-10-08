from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *



urlpatterns = [

    path("", AdvertList.as_view(), name="advert-list"),
    # path("create/", AdvertCreate.as_view()),
    # path("adverts/", UserAdvertList.as_view()),
    # path("update-advert/<int:pk>/", UserAdvertUpdate.as_view()),
    # path("delete-advert/<int:pk>/", UserAdvertDelete.as_view()),
    path("<slug:slug>/", AdvertDetail.as_view(), name="advert-detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)