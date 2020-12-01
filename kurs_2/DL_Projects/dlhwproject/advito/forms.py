from django import forms
from .models import Advert, Comment, User
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, UserCreationForm
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
