from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [

    path("", views.AdvertList.as_view(), name="advert-list"),
    path("create/", views.AdvertCreate.as_view()),
    path("adverts/", views.UserAdvertList.as_view()),
    path("update-advert/<int:pk>/", views.UserAdvertUpdate.as_view()),
    path("delete-advert/<int:pk>/", views.UserAdvertDelete.as_view()),
    path("<slug:slug>/", views.AdvertDetail.as_view(), name="advert-detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)