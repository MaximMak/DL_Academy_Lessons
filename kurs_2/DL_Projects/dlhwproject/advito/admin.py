from django.contrib import admin
from .models import Profile, Advert, Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('birth_date', 'favorite', 'avatar')

# admin.site.register(Profile)
admin.site.register(Advert)
admin.site.register(Comment)
