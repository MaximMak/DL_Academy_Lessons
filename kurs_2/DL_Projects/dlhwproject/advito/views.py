from django.db.models import Count
from django.urls import reverse

from .forms import AdvertForm, CommentForm
from .models import Advert, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, CreateView, DeleteView, UpdateView, DetailView
from .exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(ListView):
    """ Главная страница """
    model = Advert
    template_name = "advito/index.html"
    context_object_name = 'adverts'

    def get_queryset(self):
        return Advert.objects.annotate(like_num=Count('likes')).order_by('-like_num')[:3]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
           'title': 'Main Page'
        })
        return context

class AdvertDetail(DetailView):
    """" Детальная информация о объявлении """
    model = Advert
    comment_form = CommentForm
    pk_url_kwarg = 'advert_id'
    template_name = 'advito/advert_detail.html'

    def get(self, request, advert_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['coments'] = Comment.objects.filter(
            in_advert__pk=advert_id
        ).order_by('-pub_date')
        context['comment_form'] = None
        if request.user.is_authenticated:
            context['comment_form'] = self.comment_form
        return self.render_to_response(context)

    @method_decorator(login_required)
    def post(self, request, advert_id, *args, **kwargs):
        """ проверка на авторизацию, если пользователь авторизован дает возможность добавлять коментарии """
        advert = get_object_or_404(Advert, id=advert_id)
        form = self.comment_form(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.in_advert = advert
            comment.save()
            return render(request, self.template_name, context={
                'comment_form': self.comment_form,
                'advert': advert,
                'comment': advert.comment_set.order_by('-pub_date')
            })
        else:
            return render(request, self.template_name, context={
                'comment_form': form,
                'advert': advert,
                'comment': advert.comment_set.order_by('-pub_date')
            })


class AdvertCreateView(CreateView):
    """ Создание нового объявления """
    form_class = AdvertForm
    template_name = 'advito/advert_create.html'

    @method_decorator(login_required)
    def pos(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            advert = form.save(commit=False)
            author_id = request.user.id
            advert.author = request.user
            advert.save()
            context['Advert was created'] = True
            context['form'] = self.form_class
            return render(request, self.template_name, context)
        else:
            context['Advert was`nt created'] = False
            context['form'] = form
            return render(request, self.template_name, context)


class FeedView(View):
    """ Страница избранных обьявлений с фильрацие по популярности.
    Чем больше лайков, тем выше обьявление в списке"""
    template_name = "advito/feed.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            adverts = request.user.favorite.all()
            context = {
                'adverts': adverts,
            }
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)


class EditAdvert(UpdateView):
    """ Внесение изменений (редактирование) объявления """
    model = Advert
    pk_url_kwarg = 'advert_id'
    template_name = 'advito/advert_edit.html'
    form_class = AdvertForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You are not author of this Advert, editing denied!')
        return super(EditAdvert, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        advert_id = self.kwargs['advert_id']
        return reverse('advert_detail', args=(advert_id, ))


class AdvertDelete(DeleteView):
    """ Удаление обьявления """
    model = Advert
    pk_url_kwarg = 'advert_id'
    template_name = 'advito/advert_delete.html'

    def get_success_url(self):
        advert_id = self.kwargs['advert_id']
        return reverse('delete-advert-success', args=(advert_id, ))


class AdvertLike(View):
    """ Представление пометки обьявления, что оно понравилось (ставим лайк на обьявление)"""
    def get(self, request, advert_id, *args, **kwargs):
        return redirect(reverse('advert', args=(advert_id, )))

    def post(self, request, advert_id, *args, **kwargs):
        advert = get_object_or_404(Advert, id=advert_id)

        if advert.likes.filter(id=request.user.id).exists():
            like = advert.likes.get(pk=request.user.id)
            advert.likes.remove(like)
        else:
            advert.likes.add(request.user)
            advert.save()
        return redirect(request.META.get('HTTP_REFERER'), request)