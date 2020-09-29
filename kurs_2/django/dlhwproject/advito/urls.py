from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    # path('main_page/', views.about, name='Main'),
    path('adverts_all/', views.AdvertList.as_view(), name='adverts'),
    # path('ad/create/', views.create_ad, name='creating_the_ad'),
    path('<slug:category>/<slug:slug>/', views.AdvertDetail.as_view(), name='advert_detail'),
    # path('posts<int:ad_id>/edit/', views.edit_ad, name='editing_ad'),
    # path('posts<int:ad_id>/delete/', views.DeletAadvert, name='ad_delete'),
    # path('posts<int:ad_id>/favor/', views.add_to_favor, name='adding_to_favor')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)