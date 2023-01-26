from django.contrib import admin
from .models import BaseBackgroundColor, TextBackgroundColor, TextTitleFont


class BaseBackgroundColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('title', 'price')


class TextBackgroundColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('title', 'price')


class TextTitleFontAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('title', 'price')


admin.site.register(BaseBackgroundColor, BaseBackgroundColorAdmin)
admin.site.register(TextBackgroundColor, TextBackgroundColorAdmin)
admin.site.register(TextTitleFont, TextTitleFontAdmin)
