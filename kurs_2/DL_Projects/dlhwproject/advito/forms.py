from django import forms
from .models import Advert, Comment


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
                'class':'form-control', 'placeholder': 'Описание обьявления'
            }),
            'images': forms.ClearableFileInput(attrs={
                'type':'file', 'class': 'form-control-file'
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