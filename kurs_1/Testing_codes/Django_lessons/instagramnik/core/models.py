from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def avatar_path(instance, filename):
    return 'user_{0}/avatars/{1}'.format(instance.user.id, filename)


def posts_path(instance, filename):
    return 'user_{0}/posts/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    """
    Модель профиля
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    birth_date = models.DateField('Date of birth', null=True, blank=True)
    about = models.TextField('About', max_length=500, blank=True)
    avatar = models.ImageField(upload_to=avatar_path, default=None)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):

        return str(self.user.username)


class Post(models.Model):
    """
    Пост пользоваеля с картинками
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=posts_path)
    likes = models.ManyToManyField(User, related_name='Users_likes_it', blank=True)
    date_pub = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Author {} date{}'.format(self.author.username, self.date_pub)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=700)
    in_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Author {}: {}'.format(self.author.username, self.text[:10] + '...')

# Create your models here.
