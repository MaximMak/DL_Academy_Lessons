from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('about', views.about, name='about-us'),
    path('support', views.support, name='support'),
    path('ad/create/', views.create_ad, name='creating_the_ad'),
    path('posts<int:ad_id>/detail/', views.view_ad_detail, name='ad_detail'),
    path('posts<int:ad_id>/edit/', views.edit_ad, name='editing_ad'),
    path('posts<int:ad_id>/delete/', views.delete_ad, name='ad_delete'),
    path('posts<int:ad_id>/favor/', views.add_to_favor, name='adding_to_favor')


]
