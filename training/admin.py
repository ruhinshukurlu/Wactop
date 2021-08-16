from django.contrib import admin
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import *

class ImageTabularInline(admin.TabularInline):
    model = TrainingImage

class UrlTabularInline(admin.TabularInline):
    model = TrainingUrl

# class DetailTabularInline(admin.TabularInline):
#     model = TrainingDetail


class ScheduleTabularInline(admin.TabularInline):
    model = TrainingSchedule

class TrainingAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, UrlTabularInline, ScheduleTabularInline]
    list_display = ['title','organizer','training_type','datefrom','dateto']
    list_filter = ('status', )
    class Meta:
        model = Training

    def response_change(self, request, obj):
        if obj.status == 4:
            print(obj.status)
            return redirect('training:training-deny', pk = obj.pk)
        else:
            return HttpResponseRedirect('/admin/training/training/')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['training','user','message', 'rating','commented_at']



admin.site.register(Training, TrainingAdmin)
# admin.site.register(TrainingDetail)
admin.site.register(TrainingImage)
admin.site.register(TrainingUrl)
admin.site.register(TrainingSchedule)

admin.site.register([TrainingDeny])
