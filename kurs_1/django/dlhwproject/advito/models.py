from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    '''
    Модель профиля пользова теля нашего инстаграмма.
    '''
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    birth_date = models.DateField('Date of birth', null=True, blank=True)
    about = models.TextField('About', max_length=500, blank=True)
    avatar = models.ImageField(upload_to='images/', default=None)
    sale_ad = models.ManyToManyField(User, related_name='ad`s', blank=True)

    def __str__(self):
        return str(self.user.username)


class model_ad(models.Model):
    '''
    Обьявления пользователя.
    '''
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='add_images/')
    date_pud = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    type_of_ad = models.OneToOneField(max_length=20, on_delete=models.CASCADE, related_name='model_ad_type')
    category = models.ForeignKey(max_length=10, on_delete=models.CASCADE, related_name='model_ad_type')

    def __str__(self):
        return 'Author: {} date: {} Category: {} Type: {}'.format(self.author.username, self.date_pud, self.category,
                                                                  self.type_of_ad)


class ad_type(models.Model):
    '''
    Подразделения обьявлений
    '''
    sales = models.DecimalField(max_length=10, default=None)
    bay = models.DecimalField(max_length=10, default=None)
    rent = models.DecimalField(max_length=10, default=None)
    gifts = models.DecimalField(max_length=10, default=None)

    def __str__(self):
        return self


class ad_category(models.Model):
    '''
    Категория обьявления
    '''
    apartments = models.TextField(max_length=150)
    vehicles = models.TextField(max_length=150)
    land = models.DecimalField(max_length=3)
    boats = models.TextField(max_length=150)
    houses = models.TextField(max_length=150)
