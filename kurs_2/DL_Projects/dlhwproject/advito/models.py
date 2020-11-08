from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def avatar_path(instance, filename):
    return 'user{0}/avatar{1}'.format(instance.user.id, filename)


def advert_path(instance, filename):
    return 'user{0}/advert{1}'.format(instance.user.id, filename)


class Advert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    images = models.ImageField(upload_to='advert_path/')
    likes = models.ManyToManyField(User, related_name='like', blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    in_favorite = models.ManyToManyField(User, related_name='favorite', blank=True)


    def __str__(self):
        return 'author {}, date {}'.format(self.author.username, self.pub_date)

    @property
    def get_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_date = models.DateField('date_of_birth', blank=True, null=True)
    about = models.TextField('about', max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatar_path/', default=None)
    favorite = models.ManyToManyField(Advert, related_name='favorite', blank=True)

    def __str__(self):
        return str(self.user.username)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    in_post = models.ForeignKey(Advert, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Author {},  {}'.format(self.author.username, self.text[:10] + "...")