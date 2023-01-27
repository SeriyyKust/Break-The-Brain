from django.contrib import admin
from .models import Profile, Point, Visual


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'date_birth', 'photo', 'quote')
    list_display_links = ('user_id', )
    search_fields = ('user_id', )
    list_editable = ('date_birth', 'photo', 'quote')


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'number_points')
    list_display_links = ('user_id', )
    search_fields = ('user_id', )
    list_editable = ('number_points', )


@admin.register(Visual)
class VisualAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'base_background_color', 'text_background_color', 'text_title_font')
    list_display_links = ('user_id', )
    search_fields = ('user_id', )
    list_editable = ('base_background_color', 'text_background_color', 'text_title_font')
