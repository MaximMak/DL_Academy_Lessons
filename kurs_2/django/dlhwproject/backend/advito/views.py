from rest_framework import generics, permissions

from .models import Advert
from .serializers import AdvertListSer, AdvertDetailSer


class AdvertList(generics.ListAPIView):
    '''
    Все обьявления списком
    '''
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    serializer_class = AdvertListSer
    # template_name = 'profiles/advert_list.html'


class AdvertDetail(generics.RetrieveAPIView):
    '''
    Детальный просмотр обьявленя
    '''

    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    lookup_field = 'slug'
    serializer_class = AdvertListSer
    #
    # model = Advert
    # context_object_name = 'advert'
    # template_name = 'profiles/advert_detail.html'


# def index(request):
#     # advert_queryset = Advert.object.annotate(views_num=sum('views')).ordefby('-views_nums')[:7]
#     # output = ["id{}|description{}\n".format(Advert.id, Advert.description) for Advert in advert_queryset]
#     return render(request, 'profiles/index.html')
#
#
#
# def about(request):
#     return render(request, 'profiles/about.html')
#
# #
# def support(request):
#     return render(request, 'profiles/Support.html')
# #
#
# def create_ad(request, advert_id):
#     advert = Advert.object.get(id=advert_id)
#     return render(request, 'profiles/create.html')
#
#
# def edit_ad(request, advert_id):
#     ad = Advert.object.get(id=advert_id)
#     return render(request, 'profiles/edit.html')
#
#
# def DeletAdvert(request, advert_id):
#     ad = Advert.object.get(id=advert_id)
#     return render(request, 'profiles/delete.html')
#
#
# def add_to_favor(request, ad_id):
#     ad = Advert.object.get(id=ad_id)
#     return render(request, 'profiles/Support.html')



