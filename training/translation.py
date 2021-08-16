from training.models import Training #, TrainingDetail
from django.db import models
from django.db.models import fields
from modeltranslation.translator import TranslationOptions, register

# @register(TrainingDetail)
# class TrainingDetailTranslation(TranslationOptions):
#     fields = ('title', 'text',)


@register(Training)
class TrainingTranslation(TranslationOptions):
    fields = ('description', )