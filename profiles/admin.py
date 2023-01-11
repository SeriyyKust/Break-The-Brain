from django.contrib import admin
from .models import Profile, Point


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


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Point, PointAdmin)