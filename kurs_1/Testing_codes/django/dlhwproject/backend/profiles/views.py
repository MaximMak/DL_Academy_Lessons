from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerial


class ProfileDetail(generics.RetrieveAPIView):
    '''
    Профиль пользователя
    '''
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerial

    # model = Profile
    # context_object_name = 'profiles'
    # template_name = "profiles/profiles-detail.html"

    # def get_queryset(self):
    #     return Profile.objects.get(user__username=self.kwargs.get("slug"))