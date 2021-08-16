from activity.models import Activity #, ActivityDetail
from django.db import models
from django.db.models import fields
from modeltranslation.translator import TranslationOptions, register

# @register(ActivityDetail)
# class ActivityDetailTranslation(TranslationOptions):
#     fields = ('title', 'text',)


@register(Activity)
class ActivityTranslation(TranslationOptions):
    fields = ('description', )