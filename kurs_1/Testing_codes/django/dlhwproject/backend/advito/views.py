from django.shortcuts import render
from mptt import models
from rest_framework import generics, permissions
# from model.django.utils
from .models import Advert
from .serializers import AdvertListSer, AdvertDetailSer

#
# #     permission_classes = [permissions.AllowAny]
# #     queryset = Advert.objects.all()
# #     serializer_class = AdvertListSer
#     template_name = 'profiles/advert_list.html'
# #
# #
class AdvertDetail(generics.RetrieveAPIView):
    '''
    Детальный просмотр обьявленя
    '''

    model = Advert
    context_object_name = 'advert'
    template_name = 'profiles/advert_list.html'


class AdvertView(DetailView):
    model = Post
    comment_form = CommentForm
    pk_url_kwarg = 'post_id'
    template_name = 'core/post.html'

    def get(self, request, post_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['comments'] = models.Comment.objects.filter(in_post__pk=post_id).order_by('-date_publish')
        context['comment_form'] = None
        if request.user.is_authenticated:
            context['comment_form'] = self.comment_form
        return self.render_to_response(context)

    @method_decorator(login_required)
    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, pk=post_id)
        form = self.comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.date_publish = timezone.now()
            comment.author = request.user
            comment.in_post = post
            comment.save()
            return render(request=request, template_name=self.template_name, context={'comment_form': self.comment_form,
                                                                                      'post': post,
                                                                                      'comments': post.comment_set.order_by(
                                                                                       '-date_publish')})
        else:
            return render(request=request, template_name=self.template_name, context={'comment_form': form,
                                                                                      'post': post,
                                                                                      'comments': post.comment_set.order_by(
                                                                                       '-date_publish')})


#     #
class AdvertList():
    '''
    Все обьявления списком
    '''
    model = Advert
    context_object_name = 'advert'
    template_name = 'profiles/advert_list.html'


def index(request):
    # advert_queryset = Advert.object.annotate(views_num=sum('views')).ordefby('-views_nums')[:7]
    # output = ["id{}|description{}\n".format(Advert.id, Advert.description) for Advert in advert_queryset]
    return render(request, 'profiles/index.html')



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



