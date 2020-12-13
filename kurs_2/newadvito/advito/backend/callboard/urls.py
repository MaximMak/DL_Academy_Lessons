from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("adverts/", views.AdvertList.as_view(), name='advert_list'),
    path("<slug:category>/<slug:slug>/", views.AdvertDetail.as_view(), name="advert_detail"),
    # path("update-advert/<int:pk>/", views.UserAdvertUpdate.as_view()),
    # path("delete-advert/<int:pk>/", views.UserAdvertDelete.as_view()),
]
