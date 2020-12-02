from django.contrib import admin
from .models import Profile, Advert, Comment
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'about', 'birth_date', 'id')
#     search_fields = ('user', 'about', 'birth_date', 'id')

admin.site.register(Profile)
admin.site.register(Advert)
admin.site.register(Comment)
