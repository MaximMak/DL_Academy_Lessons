from django.conf.urls import url
from .login_views import LoginView, SignUpView, logout_view
from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    path('feed/', views.FeedView.as_view(), name='feed'),
    path('adverts/create/', views.AdvertCreateView.as_view(), name='create_advert'),
    path('adverts/<int:advert_id>/', views.AdvertDetail.as_view(), name='advert_detail'),
    path('adverts/<int:advert_id>/edit/', views.EditAdvert.as_view(), name='advert-edit'),
    path('adverts/<int:advert_id>/delete/', views.AdvertDelete.as_view(), name='advert-delete'),
    path('adverts/<int:advert_id>/delete_success/', TemplateView.as_view(
        template_name='advito/delete_success.html'), name='delete-advert-success'
        ),
    path('adverts/<int:advert_id>/like/', views.AdvertLike.as_view(), name='advert_like'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', SignUpView.as_view(), name='register'),

]
