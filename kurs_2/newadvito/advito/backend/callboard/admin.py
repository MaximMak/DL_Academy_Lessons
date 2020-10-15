from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Advert, FiltersAdvert, AdvertDate



@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """
    Категории
    """
    list_display = ("name", "parent", "id")
    mptt_level_ident = 20
    prepopulated_fields = {"slug": ('name',)}
    search_fields = ("name", "parent")


@admin.register(FiltersAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    """
    Сортировочный фильтр
    """
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ('name',)}
    search_fields = ("name",)


@admin.register(AdvertDate)
class AdvertDateAdmin(admin.ModelAdmin):
    """
    Срок размещения
    """
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ('name',)}
    search_fields = ("name",)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """
    Обьявления
    """
    list_display = ("id", "author", "category", "subject", "filters", "date", "price", "created", "moderation")
    list_display_links = ("subject",)
    list_filter = ("author", "filters", "category", "date", "price")
    prepopulated_fields = {"slug": ("author", "subject")}
    search_fields = ("user", "category", "subject", "date", "created")
#
#
# admin.site.register(Profile)
# admin.site.register(Comments)
