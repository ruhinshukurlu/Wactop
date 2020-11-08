from django.contrib import admin
from .models import *
from account.forms import *

class ImageTabularInline(admin.TabularInline):
    model = OrganizerImage

class UrlTabularInline(admin.TabularInline):
    model = OrganizerUrl

class OrganizerAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, UrlTabularInline]
    list_display = ['user','viewcount']

    # class Meta:
    #     model = Organizer
    


admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Guide)
admin.site.register(Instructor)
admin.site.register(OrganizerType)
admin.site.register(OrganizerImage)
admin.site.register(OrganizerUrl)
admin.site.register(Contact)