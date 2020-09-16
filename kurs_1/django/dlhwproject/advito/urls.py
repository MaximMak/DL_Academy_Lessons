from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('about', views.about, name='about-us'),
    url('support', views.support, name='support')


]
