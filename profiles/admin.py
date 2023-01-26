from django.contrib import admin
from .models import Profile, Point, Visual


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'date_birth', 'photo', 'quote')
    list_display_links = ('user_id', )
    search_fields = ('user_id', )
    list_editable = ('date_birth', 'photo', 'quote')


class PointAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'number_points')
    list_display_links = ('user_id', )
    search_fields = ('user_id', )
    list_editable = ('number_points', )


class VisualAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'base_background_color', 'text_background_color', 'text_title_font')
    list_display_links = ('user_id', )
    search_fields = ('user_id', )
    list_editable = ('base_background_color', 'text_background_color', 'text_title_font')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Visual, VisualAdmin)
