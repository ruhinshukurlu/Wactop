from django.contrib import admin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
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

    def response_change(self, request, obj):
        if obj.status == 4:
            print(obj.status)
            return redirect('activity:activity-deny', pk = obj.pk)
        else:
            return HttpResponseRedirect('/admin/activity/activity/')




admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityDetailAZ)
admin.site.register(ActivityDetailEN)
admin.site.register(ActivityDetailRU)
admin.site.register(ActivityImage)
admin.site.register(ActivityUrl)
admin.site.register(ActivitySchedule)
admin.site.register(ActivityComment)
admin.site.register([ActivityDeny])

