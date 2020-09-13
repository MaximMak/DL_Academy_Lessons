from django.contrib import admin
from .models import Profile, Comment, Post


admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Post)

# Register your models here.
