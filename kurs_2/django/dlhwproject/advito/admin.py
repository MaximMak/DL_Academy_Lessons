from django.contrib import admin
from .models import Profile, Category, Ad, type_ad, DateAd


admin.site.register(Profile)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(DateAd)
admin.site.register(type_ad)


