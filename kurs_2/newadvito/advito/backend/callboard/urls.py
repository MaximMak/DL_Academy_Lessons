from django.conf.urls import url
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    path('adverts/', AdvertList.as_view(), name='advert-list'),
    path("<slug:slug>/", AdvertDetail.as_view(), name="advert-detail"),
    # path("adverts/", AdvertList.as_view()),
    # path("update-advert/<int:pk>/", UserAdvertUpdate.as_view()),
    # path("delete-advert/<int:pk>/", UserAdvertDelete.as_view()),
    # path("<slug:slug>/", AdvertDetail.as_view(), name="advert-detail"),
]
