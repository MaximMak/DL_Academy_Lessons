# Generated by Django 3.0.10 on 2020-11-08 09:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advito', '0007_auto_20201102_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='in_favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
