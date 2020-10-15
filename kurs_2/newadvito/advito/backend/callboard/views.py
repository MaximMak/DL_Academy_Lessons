from django.forms import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Advert


class AdvertList(ListView):
    '''
    Все обьявления списком
    '''
    model = Advert
    queryset = Advert.objects.all()
    template_name = 'advert_list.html'


class AdvertDetail(DetailView):
    '''
    Детальный просмотр обьявленя
    '''

    model = Advert
    queryset = Advert.objects.all()
    template_name = 'advert_detail.html'


def index_view(request):
    return render(request, 'index.html')


def index(request):
    # advert_queryset = Advert.object.annotate(views_num=sum('views')).ordefby('-views_nums')[:7]
    # output = ["id{}|description{}\n".format(Advert.id, Advert.description) for Advert in advert_queryset]
    return render(request, 'index.html')

def about(request):
    return render(request, 'profiles/about.html')

#
def support(request):
    return render(request, 'profiles/Support.html')

#

def create_ad(request, advert_id):
    advert = Advert.object.get(id=advert_id)
    return render(request, 'profiles/create.html')

def edit_ad(request, advert_id):
    ad = Advert.object.get(id=advert_id)
    return render(request, 'profiles/edit.html')

def DeletAdvert(request, advert_id):
    ad = Advert.object.get(id=advert_id)
    return render(request, 'profiles/delete.html')

def add_to_favor(request, ad_id):
    ad = Advert.object.get(id=ad_id)
    return render(request, 'profiles/Support.html')