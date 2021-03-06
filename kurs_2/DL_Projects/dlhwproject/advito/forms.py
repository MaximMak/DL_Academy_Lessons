from django import forms
from .models import Advert, Comment, User
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
)


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль:', 'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтвердите пароль:', 'class': 'form-control'
        }),
        help_text="Введите повторно тотже пароль, что и выше:"
    )

    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Email', 'autofocus': True
            })
        }


class UpdateProfile(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'profile_Names', 'placeholder': 'Username', 'autofocus': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'profile_email', 'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'profile_Names', 'placeholder': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'profile_Names', 'placeholder': 'last_name'
            }),
            'About': forms.Textarea(attrs={
            'class': 'profile_about textarea', 'placeholder': 'last_name'
        })
        }

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        last_name = self.cleaned_data.get('last_name')
        first_name = self.cleaned_data.get('first_name')
        about = self.cleaned_data.get('about')


        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        profile = super(UserChangeForm, self).save(commit=False)
        profile.email = self.cleaned_data['email']

        if commit:
            profile.save()

        return profile

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'autofocus': True, 'placeholder': 'Имя', 'class': 'form-control'
        }))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль', 'class': 'form-control'
        }))
    error_messages = {
        'invalid_login': 'Некорректно введен логин или пароль'
    }


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['description', 'images']
        labels = {
            'description': 'Описание обьявления',
            'images': 'Выберите картинку'
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Описание обьявления'
            }),
            'images': forms.ClearableFileInput(attrs={
                'type': 'file', 'class': 'form-control-file'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widget = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Comment text'
            })
        }
