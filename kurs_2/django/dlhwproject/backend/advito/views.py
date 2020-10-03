from rest_framework import generics, permissions

from .models import Advert
from .serializers import AdvertListSerial, AdvertDetailSerial


class AdvertList(generics.ListAPIView):
    '''
    Все обьявления списком
    '''
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    serializer_class = AdvertListSerial
    # template_name = 'advito/advert_list.html'


class AdvertDetail(generics.RetrieveAPIView):
    '''
    Детальный просмотр обьявленя
    '''

    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    lookup_field = 'slug'
    serializer_class = AdvertListSerial
    #
    # model = Advert
    # context_object_name = 'advert'
    # template_name = 'advito/advert_detail.html'


# def index(request):
#     # advert_queryset = Advert.object.annotate(views_num=sum('views')).ordefby('-views_nums')[:7]
#     # output = ["id{}|description{}\n".format(Advert.id, Advert.description) for Advert in advert_queryset]
#     return render(request, 'advito/index.html')
#
#
#
# def about(request):
#     return render(request, 'advito/about.html')
#
# #
# def support(request):
#     return render(request, 'advito/Support.html')
# #
#
# def create_ad(request, advert_id):
#     advert = Advert.object.get(id=advert_id)
#     return render(request, 'advito/create.html')
#
#
# def edit_ad(request, advert_id):
#     ad = Advert.object.get(id=advert_id)
#     return render(request, 'advito/edit.html')
#
#
# def DeletAdvert(request, advert_id):
#     ad = Advert.object.get(id=advert_id)
#     return render(request, 'advito/delete.html')
#
#
# def add_to_favor(request, ad_id):
#     ad = Advert.object.get(id=ad_id)
#     return render(request, 'advito/Support.html')



