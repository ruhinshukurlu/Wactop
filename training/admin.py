from django.contrib import admin
from .models import *

class ImageTabularInline(admin.TabularInline):
    model = TrainingImage

class UrlTabularInline(admin.TabularInline):
    model = TrainingUrl

class DetailAZTabularInline(admin.TabularInline):
    model = TrainingDetailAZ

class DetailENTabularInline(admin.TabularInline):
    model = TrainingDetailEN

class DetailRUTabularInline(admin.TabularInline):
    model = TrainingDetailRU

class ScheduleTabularInline(admin.TabularInline):
    model = TrainingSchedule

class TrainingAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, DetailAZTabularInline, DetailENTabularInline, DetailRUTabularInline, UrlTabularInline, ScheduleTabularInline]
    class Meta:
        model = Training



admin.site.register(Training, TrainingAdmin)
admin.site.register(TrainingDetailAZ)
admin.site.register(TrainingDetailEN)
admin.site.register(TrainingDetailRU)
admin.site.register(TrainingImage)
admin.site.register(TrainingUrl)
admin.site.register(TrainingSchedule)