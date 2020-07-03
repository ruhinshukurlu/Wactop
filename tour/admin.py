from django.contrib import admin
from .models import *

class ImageTabularInline(admin.TabularInline):
    model = TourImage

class UrlTabularInline(admin.TabularInline):
    model = TourUrl

class DetailAZTabularInline(admin.TabularInline):
    model = TourDetailAZ

class DetailENTabularInline(admin.TabularInline):
    model = TourDetailEN

class DetailRUTabularInline(admin.TabularInline):
    model = TourDetailRU

class ScheduleTabularInline(admin.TabularInline):
    model = TourSchedule

class TourAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, DetailAZTabularInline, DetailENTabularInline, DetailRUTabularInline, UrlTabularInline, ScheduleTabularInline]
    list_filter = ('status', )
    class Meta:
        model = Tour



admin.site.register(Type)

admin.site.register(Tour, TourAdmin)
admin.site.register(TourDetailAZ)
admin.site.register(TourDetailEN)
admin.site.register(TourDetailRU)
admin.site.register(TourImage)
admin.site.register(TourUrl)
admin.site.register(TourSchedule)