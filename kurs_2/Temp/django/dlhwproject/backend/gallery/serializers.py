from rest_framework import serializers

from .models import *


class PhotoSerial(serializers.ModelSerializer):
    """
    Для вывода изображения
    """

    class Meta:
        model = Photo
        fields = ("image",)


class GallerySerial(serializers.ModelSerializer):
    """
    Для вывода галереи
    """
    photos = PhotoSerial(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ("photos", )