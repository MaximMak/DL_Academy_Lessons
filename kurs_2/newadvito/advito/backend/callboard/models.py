from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class FiltersAdvert(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"


class AdvertDate(models.Model):
    """Срок для объявления"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"
        ordering = ["id"]


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
        related_name='children',
        verbose_name='parent'
    )
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_inspection_by = ['name']
        verbose_name = "Категория"


class Advert(models.Model):
    '''
    Обьявления пользователя.
    '''
    author = models.ForeignKey(User, verbose_name="Автор объявления", on_delete=models.CASCADE)
    filters = models.ForeignKey(FiltersAdvert, verbose_name="Фильтр", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    date = models.ForeignKey(AdvertDate, verbose_name="Срок размещения", on_delete=models.CASCADE, null=True)
    subject = models.CharField("Тема обьявления", max_length=200)
    description = models.TextField("Текст обьявления", max_length=1000)
    images = models.ForeignKey(
        'gallery.Gallery',
        verbose_name="Изображения",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    file = models.FileField("Файл", upload_to="media/advito_file/", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=20, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    moderation = models.BooleanField("Модерация", default=False)
    # comments = models.TextField("Комментарии к объявлению", max_length=250)
    slug = models.SlugField("url", max_length=200, unique=True, blank=True, null=True)
    in_favorite = models.ManyToManyField(User, related_name='favorite_posts', blank=True)
    views_num = models.PositiveIntegerField(blank=True, null=True)

    def views_num_count(self):
        Advert.objects.filter(pk=Advert.pk).update(views=F('views_num') + 1)
        Advert.views_num += 1

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('advert_detail', kwargs={"category": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"


class Comments(models.Model):
    """
    Комментарии к обьявлению
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    in_advert = models.ForeignKey(Advert, related_name='Advert_comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=250, blank=False)
    date_publish = models.TimeField(default=timezone.now)

    def __str__(self):
        return "{0}: {1}".format(self.author, self.text[:10] + "...")
