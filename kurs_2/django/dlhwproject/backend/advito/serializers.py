from rest_framework import serializers

from ..gallery.serializers import GallerySerial
from .models import *


class CategorySerial(serializers.ModelSerializer):
    """
    Для вывода категорий
    """

    class Meta:
        model = Category
        fields = ("name", )


class FiltersSerial(serializers.ModelSerializer):
    """
    Для вывода категорий
    """

    class Meta:
        model = FiltersAdvert
        fields = ("name", )


class AdvertListSerial(serializers.ModelSerializer):
    """Для вывода списка объявлений"""
    category = CategorySerial()
    filters = FiltersSerial()
    images = GallerySerial(read_only=True)

    class Meta:
        model = Advert
        fields = ("id", "category", "filters", "subject", "images",
                  "price", "created", "slug")


class AdvertDetailSerial(serializers.ModelSerializer):
    """Для вывода полного объявления"""
    category = CategorySerial()
    filters = FiltersSerial()
    images = GallerySerial(read_only=True)

    class Meta:
        model = Advert
        fields = ("category", "filters", "subject", "description",
                  "images", "file", "price", "created", "user")