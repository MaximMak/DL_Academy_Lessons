from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, DetailView
from django.urls import reverse

from.models import Profile

from .forms import LoginForm, SignUpForm, UpdateProfile
from django.contrib.auth import authenticate, login, logout


class LoginView(LoginView):
    """ Представление авторизации пользователя на сайте """
    template_name = 'my_auth/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('index'), request)
            else:
                context = {
                    'form': form
                }
                return render(request, self.template_name, context)
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class SignUpView(View):
    """ Представление создания нового пользователя на сайте"""
    template_name = 'my_auth/signup.html'
    registration_form = SignUpForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.registration_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ функция проверк формы на соответствие (валидность) и последующее сохранения в случае соответствия """
        user_form = self.registration_form(data=request.POST)
        registered = False
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']
            user.save()
            registered = True
            return render(request, self.template_name, {'registered': registered})
        else:
            return render(
                request, self.template_name, {
                    'form': user_form, 'registered': registered
                }
            )


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


class ProfileView(DetailView):
    """ представление детального вида профиля"""
    model = Profile
    template_name = 'my_auth/profile.html'

    def get_object(self):
        """ вывод ошибки в случае отсутствия профиля """
        return get_object_or_404(Profile, user__id=self.kwargs['user_id'])

class UpdateProfileView(View):
    """ представения для изменения профиля пользователя """
    template_name = 'my_auth/update_profile.html'
    update_form = UpdateProfile

    def get(self, request, *args, **kwargs):
        """ функция сохренения формы"""
        context = {
            'form': self.update_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ функция проверк формы на соответствие (валидность) и последующее сохранения в случае соответствия """
        UpPf_form = self.update_form(data=request.POST)
        if UpPf_form.is_valid():
            user = UpPf_form.save(commit=False)
            user.email = UpPf_form.cleaned_data['email']
            user.first_name = UpPf_form.cleaned_data['first_name']
            user.email = UpPf_form.cleaned_data['last_name']
            user.save()
            registered = True
            return render(request, self.template_name, {'registered': registered})
        else:
            """ Возврат к ввобу формы в случае не соответствия формы (если не валидна)"""
            return render(
                request, self.template_name, {
                    'form': UpPf_form})
