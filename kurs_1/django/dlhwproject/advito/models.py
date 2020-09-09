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


class sale_ad(models.Model):
    '''
    Обьявления пользователя.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='add_images/')
    date_pud = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    type_of_ad = models.TextField(max_length=20)
    category = models.ForeignKey(max_length=20)


    def __str__(self):
        return 'Author {} date {}'.format(self.author.username, self.date_pud)

