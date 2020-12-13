from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import View, DetailView
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.http import Http404

from .models import Profile
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm, UpdateProfile
from django.contrib.auth import authenticate, login, logout


class LoginView(LoginView):
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
    template_name = 'my_auth/signup.html'
    registration_form = SignUpForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.registration_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
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
    model = Profile
    context_object_name = 'profile'
    template_name = 'my_auth/profile.html'
    slug_field = 'user__id'
    slug_url_kwarg = 'user_id'

    def get_object(self, queryset=None):
        profile = Profile.objects.get_or_create(user_id=self.kwargs['user_id'])[0]
        return profile

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data()
        return context


class UpdateProfileView(UpdateView):
    model = User
    template_name = 'my_auth/update_profile.html'
    form_class = UpdateProfile
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object():
            raise Http404('You have no permissions to update this profile!')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user != self.get_object():
            raise Http404('You have no permissions to update this profile!')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object == self.request.user:
            # Do any custom stuff here
            self.object.save()
        return super().form_valid(form)

