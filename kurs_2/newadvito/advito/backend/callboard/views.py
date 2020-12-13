from django.db.models import Sum
from django.forms import models
from django.shortcuts import render
from django.template import loader
from django.views import View
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
    context_object_name = 'advert_detail'
    template_name = 'advert_detail.html'

#
# def index_view(request):
#     return render(request, 'index.html')


class IndexView(ListView):
    model = Advert
    queryset = Advert.objects.all()
    template_name = "index.html"
    context_object_name = "popular_adverts"


    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         adverts = request.user..all()
    #         context = {
    #             'adverts': adverts,
    #         }
    #         return render(request, self.template_name, context)
    #     else:
    #         return render(request, self.template_name)


class FeedView(View):
    template_name = "advito/feed.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            adverts = request.user.like.all()
            context = {
                'adverts': adverts,
            }
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)



def about(request):
    return render(request, 'profiles/about.html')

#
def support(request):
    return render(request, 'profiles/Support.html')





#
#
# def create_ad(request, advert_id):
#     advert = Advert.object.get(id=advert_id)
#     return render(request, 'profiles/create.html')
#
# def edit_ad(request, advert_id):
#     ad = Advert.object.get(id=advert_id)
#     return render(request, 'profiles/edit.html')
#
# def DeletAdvert(request, advert_id):
#     ad = Advert.object.get(id=advert_id)
#     return render(request, 'profiles/delete.html')
#
# def add_to_favor(request, ad_id):
#     ad = Advert.object.get(id=ad_id)
#     return render(request, 'profiles/Support.html')