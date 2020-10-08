import os

from PIL import Image
from django.db import models

from django.utils import timezone


def get_path_upload_image(file):
    """
    Представление для формата сохранения файлов
    """
    date = timezone.now().strftime("%Y-%m-%d")
    time = timezone.now().strftime("%H-%M-%S")
    end_extention = file.split('.')[1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + time + '.' + end_extention
    return os.path.join('photos', '{}', '{}').format(date, file_name)


class Photo(models.Model):
    """
    Фото
    """
    name = models.CharField("Имя", max_length=50)
    image = models.ImageField("Фото", upload_to="gallery/")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     img = Image.open(self.image.get_path_upload_image())
    #     super().save(*args, **kwargs)
    #     # if self.image:
    #     #     if img.height > 200 or img.width > 200:
    #     #         output_size = (200, 200)
    #     #         img.thumbnail(output_size)
    #     #         img.save(self.avatar.path)

    def save(self, *args, **kwargs):
        self.image.name = get_path_upload_image(self.image.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Gallery(models.Model):
    """
    Галерея
    """
    name = models.CharField("Имя", max_length=50)
    photos = models.ManyToManyField(Photo, verbose_name="Фотографии")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
