from django.contrib import admin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import *

class ImageTabularInline(admin.TabularInline):
    model = TourImage

class UrlTabularInline(admin.TabularInline):
    model = TourUrl

class DetailTabularInline(admin.TabularInline):
    model = TourDetail


class ScheduleTabularInline(admin.TabularInline):
    model = TourSchedule

class TourAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, DetailTabularInline, UrlTabularInline, ScheduleTabularInline]
    list_filter = ('status', )
    list_display = ['title','organizer','tour_type','datefrom','dateto']
    class Meta:
        model = Tour

    def response_change(self, request, obj):
        if obj.status == 4:
            print(obj.status)
            return redirect('tour:tour-deny', pk = obj.pk)
        else:
            return HttpResponseRedirect('/admin/tour/tour/')


@admin.register(TourComment)
class TourCommentAdmin(admin.ModelAdmin):
    list_display = ['tour','user','message', 'rating','commented_at']
    

admin.site.register(TourType)

admin.site.register(Tour, TourAdmin)
admin.site.register(TourDetail)
admin.site.register(TourImage)
admin.site.register(TourUrl)
admin.site.register(TourSchedule)

admin.site.register([TourDeny])