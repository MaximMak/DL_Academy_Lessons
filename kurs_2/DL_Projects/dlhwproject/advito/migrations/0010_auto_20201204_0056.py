# Generated by Django 3.0.10 on 2020-12-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advito', '0009_auto_20201116_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(blank=True, max_length=50, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(blank=True, max_length=50, verbose_name='last_name'),
        ),
    ]
