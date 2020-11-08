from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('adverts/create/', views.AdvertCreateView.as_view(), name='create_advert'),
    path('adverts/<int:advert_id>/', views.AdvertDetail, name='advert_detail'),
    path('adverts/<int:advert_id>/edit/', views.EditAdvert.as_view(), name='edit_advert'),
    path('adverts/<int:advert_id>/delete/', views.AdvertDelete.as_view(), name='advert-delete'),
    path('adverts/<int:advert_id>/delete_success/', TemplateView.as_view(template_name='advert/delete_success.html'), name='delete-advert-success'),
    path('adverts/<int:advert_id>/like/', views.AdvertLike.as_view, name='advert_like'),
]
