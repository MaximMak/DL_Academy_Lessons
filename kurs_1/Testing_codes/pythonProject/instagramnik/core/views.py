from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Profile, Comment
from django.db.models import Count
from django.template import loader


def index(request):
    post_queryset = Post.objects.annotate(like_nums=Count('likes')).order_by('-like_nums')[:3]
    template = loader.get_template('core/index.html')
    context = {
        'posts': post_queryset,
    }
    return HttpResponse(template.render(context))


def feed(request):
    feed_queryset = Post.objects.filter(author__in=request.user.user_profile.friends.all())
    output = ["id:{}|description:{}\n".format(post.id, post.description) for post in feed_queryset]
    return HttpResponse(output)


def post_detail(request, post_id):
    post = Post.object.get(id=post_id)
    response = "Author:{}| description:{}".format(post.author, post.description)
    return HttpResponse(response)


def post_edit(request, post_id):
    post = Post.object.get(id=post_id)
    response = "Deleting Author:{}| description:{}".format(post.author, post.description)
    return HttpResponse(response)


def post_create(request, post_id):
    post = Post.object.get(id=post_id)
    response = "Deleting Author:{}| description:{}".format(post.author, post.description)
    return HttpResponse(response)


def post_delete(request, post_id):
    response = "Post deleting # {}".format(post_id)
    return HttpResponse(response)


def like_post(request, post_id):
    response = "Liking the post # {}".format(post_id)
    return HttpResponse(response)
