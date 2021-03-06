from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



def avatar_path(instance, file_name):
    return 'user{0}/avatar/{1}'.format(instance.user.id, file_name)


def ad_img_path(instance, file_name):
    return 'user{0}/ad_img/{1}'.format(instance.user.id, file_name)


class Profile(models.Model):
    '''
    Модель профиля пользователя
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_date = models.DateField('Date of birth', null=True, blank=True)
    about = models.TextField('About', max_length=500, blank=True)
    avatar = models.ImageField(upload_to=avatar_path, default=None)
    favor_ad = models.ManyToManyField(User, related_name='favorite', blank=True)
    count_of_ad = models.DecimalField(max_digits=3, blank=True, decimal_places=2)

    def __str__(self):
        return str(self.user.username)


class type_ad(models.Model):
    sales = models.TextField(max_length=7)
    bay = models.TextField(max_length=7)


class ad_category(models.Model):
    apartments = models.TextField(max_length=150)
    vehicles = models.TextField(max_length=150)


class Ad(models.Model):
    '''
    Обьявления пользователя.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_ad = models.ForeignKey(type_ad, on_delete=models.CASCADE)
    category = models.ForeignKey(ad_category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=ad_img_path)
    date_pud = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Author {} date{}'.format(self.author.username, self.date_pub)

    @property
    def get_favor(self):
        return self.favor.count()