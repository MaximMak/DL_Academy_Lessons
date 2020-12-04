from django.conf.urls import url
from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetCompleteView
)

from django.views.generic import TemplateView

from .login_views import UpdateProfileView
from . import views, login_views

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
    path('login/', login_views.LoginView.as_view(), name='login'),
    path('logout/', login_views.logout_view, name='logout'),
    path('registration/', login_views.SignUpView.as_view(), name='register'),
    path('profile/<int:user_id>/', login_views.ProfileView.as_view(), name='profile'),
    # path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),

    path('password-reset/', PasswordResetView.as_view(
        success_url=reverse_lazy('password_reset_done'), template_name='my_auth/pass-reset.html'
    ), name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='my_auth/password_reset_done.html'
    ), name='password_reset_done'),

    path('password-reset/<str:uidb64>/<slug:token>', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('password_reset_complete'),
    ), name='password_reset_confirm'),

    path('password-reset/complite/', PasswordResetCompleteView.as_view(
    template_name='my_auth/login.html'
    ), name='password_reset_complete'),
]
