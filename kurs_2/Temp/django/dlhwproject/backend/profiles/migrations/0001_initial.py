# Generated by Django 3.0.10 on 2020-12-11 21:30

import backend.profiles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='О себе')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=backend.profiles.models.avatar_path, verbose_name='Аватар')),
                ('email_two', models.EmailField(max_length=254, verbose_name='Поля доп мыла')),
                ('phone', models.CharField(max_length=25, verbose_name='Поле для телефона')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('slug', models.SlugField(default='', verbose_name='url')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиля',
            },
        ),
    ]
