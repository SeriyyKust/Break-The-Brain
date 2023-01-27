from django.contrib import admin
from .models import BaseBackgroundColor, TextBackgroundColor, TextTitleFont


@admin.register(BaseBackgroundColor)
class BaseBackgroundColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('title', 'price')


@admin.register(TextBackgroundColor)
class TextBackgroundColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('title', 'price')


@admin.register(TextTitleFont)
class TextTitleFontAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('title', 'price')
