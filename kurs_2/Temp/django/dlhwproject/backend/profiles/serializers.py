from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class ProfileSerial(serializers.ModelSerializer):
    """
    Профиль пользователя
    """
    user = UserSerial()

    class Meta:
        model = Profile
        fields = ("user", "avatar", "email_tvo", "phone", "first_name", "last_name")


class ProfileUpdateSer(serializers.ModelSerializer):
    """
    Редактирование профиль пользователя
    """

    class Meta:
        model = Profile
        fields = ("avatar", "email_tvo", "phone", "first_name", "last_name")


class AvatarUpdateSer(serializers.ModelSerializer):
    """
    Редактирование аватара
    """

    class Meta:
        model = Profile
        fields = ("avatar", )

