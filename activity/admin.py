from django.contrib import admin
from .models import *

class ImageTabularInline(admin.TabularInline):
    model = ActivityImage

class UrlTabularInline(admin.TabularInline):
    model = ActivityUrl

class DetailAZTabularInline(admin.TabularInline):
    model = ActivityDetailAZ

class DetailENTabularInline(admin.TabularInline):
    model = ActivityDetailEN

class DetailRUTabularInline(admin.TabularInline):
    model = ActivityDetailRU

class ScheduleTabularInline(admin.TabularInline):
    model = ActivitySchedule

class ActivityAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, DetailAZTabularInline, DetailENTabularInline, DetailRUTabularInline, UrlTabularInline, ScheduleTabularInline]
    class Meta:
        model = Activity



admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityDetailAZ)
admin.site.register(ActivityDetailEN)
admin.site.register(ActivityDetailRU)
admin.site.register(ActivityImage)
admin.site.register(ActivityUrl)
admin.site.register(ActivitySchedule)