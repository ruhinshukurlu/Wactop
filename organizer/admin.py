from django.contrib import admin
from .models import *

class ImageTabularInline(admin.TabularInline):
    model = OrganizerImage

class UrlTabularInline(admin.TabularInline):
    model = OrganizerUrl

class OrganizerAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, UrlTabularInline]
    list_filter = ('registered', )
    class Meta:
        model = Organizer



admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(OrganizerType)
admin.site.register(OrganizerImage)
admin.site.register(OrganizerUrl)