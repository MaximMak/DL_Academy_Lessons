from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = {
    url(r'^$', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('posts/create/', views.post_create, name='creating_the_post'),
    path('posts<int:post_id>/detail/', views.post_detail, name='post_detail'),
    path('posts<int:post_id>/edit/', views.post_edit, name='editing_post'),
    path('posts<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('posts<int:post_id>/likes/', views.like_post, name='post_like')
}