from django.conf.urls import url
from django.urls import path
from .views import AdvertList, AdvertDetail, IndexView
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("adverts/", AdvertList.as_view(), name='advert_list'),
    path("<slug:category>/<slug:slug>/", AdvertDetail.as_view(), name="advert_detail"),
    # path("update-advert/<int:pk>/", UserAdvertUpdate.as_view()),
    # path("delete-advert/<int:pk>/", UserAdvertDelete.as_view()),
]
