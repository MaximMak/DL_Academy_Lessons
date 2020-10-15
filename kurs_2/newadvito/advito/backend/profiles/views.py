from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile


class ProfileDetail(DetailView):
    '''
    Профиль пользователя
    '''
    model = Profile
    context_object_name = 'profiles'
    template_name = "frontend/profiles_detail.html"

    def get_queryset(self):
        return Profile.objects.get(user__username=self.kwargs.get("slug"))