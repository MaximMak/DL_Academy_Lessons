from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


def avatar_path(instance, file_name):
    return 'user{0}/avatar/{1}'.format(instance.user.id, file_name)


def ad_img_path(instance, file_name):
    return 'user{0}/ad_img/{1}'.format(instance.user.id, file_name)


class Category(MPTTModel):
    """
    Категории обьявлений
    """
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMata:
        order_inspection_by = ['name']


class Profile(models.Model):
    '''
    Модель профиля пользователя
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_date = models.DateField('Date of birth', null=True, blank=True)
    about = models.TextField('About', max_length=500, blank=True)
    avatar = models.ImageField(upload_to=avatar_path, default=None)
    profile_ad = models.ManyToManyField(User, related_name='My_ad', blank=True)

    def __str__(self):
        return str(self.user.username)


class type_ad(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категори"


class DateAd(models.Model):
    """Срок для объявления"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"
        ordering = ["id"]


class Ad(models.Model):
    '''
    Обьявления пользователя.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_ad = models.ForeignKey(type_ad, related_name='type_of_ad', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.ForeignKey(DateAd, verbose_name="Срок", on_delete=models.CASCADE, default=timezone.now)
    description = models.TextField("Текст обьявления", max_length=1000)
    subject = models.CharField("Тема обьявления", max_length=1000)
    images = models.ForeignKey(
        'gallery.Gallery',
        verbose_name="Изображения",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    date_pud = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    in_favor = models.ManyToManyField(User, related_name='favor_ad', blank=True)
    moderation = models.BooleanField("Модерация", default=False)
    slug = models.SlugField("url", max_length=200, unique=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"
