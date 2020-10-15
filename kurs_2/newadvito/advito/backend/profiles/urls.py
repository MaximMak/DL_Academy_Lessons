from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    # url('', views.ProfileDetail, name='profiles')
    path("<int:pk>/", views.ProfileDetail.as_view(), name="profiles-detail")
]

