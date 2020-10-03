from rest_framework import serializers

from ..gallery.serializers import GallerySerial
from .models import *


class CategorySer(serializers.ModelSerializer):
    """Для вывода категорий"""
    class Meta:
        model = Category
        fields = ("name", )


class FilterAdvertSer(serializers.ModelSerializer):
    """Для вывода фильтров"""
    class Meta:
        model = FiltersAdvert
        fields = ("name", )


class AdvertListSer(serializers.ModelSerializer):
    """Для вывода списка объявлений"""
    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySerial(read_only=True)

    class Meta:
        model = Advert
        fields = ("id", "category", "filters", "subject", "images", "price", "created", "slug")


class AdvertDetailSer(serializers.ModelSerializer):
    """Для вывода полного объявления"""
    category = CategorySer()
    filters = FilterAdvertSer()
    images = GallerySerial(read_only=True)

    class Meta:
        model = Advert
        fields = (
            "category",
            "filters",
            "subject",
            "description",
            "images",
            "file",
            "price",
            "created",
            "user"
        )


class AdvertCreateSer(serializers.ModelSerializer):
    """Добавление объявления"""
    #images = GallerySer()

    class Meta:
        model = Advert
        fields = (
            "category",
            "filters",
            "date",
            "subject",
            "description",
            "price",
            "images"
        )

    def create(self, request):
        request["user"] = self.context['request'].user
        advert = Advert.objects.create(**request)
        return advert