from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


def avatar_path(instance, file_name):
    return 'profile{0}/avatar/{1}'.format(instance.user.id, file_name)


class Profile(models.Model):
    """
    Модель профиля пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    about = models.TextField('О себе', max_length=500, blank=True)
    avatar = models.ImageField('Аватар', upload_to=avatar_path, blank=True, null=True)
    email_two = models.EmailField('Поля доп мыла')
    phone = models.CharField('Поле для телефона', max_length=25)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    slug = models.SlugField('url', max_length=50, default='')

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("profile-detail", kwargs={'name': self.user.username})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Создание профиля пользователя при регистрации
    """
    if created:
        Profile.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()