from tour.models import Tour, TourDetail
from django.db import models
from django.db.models import fields
from modeltranslation.translator import TranslationOptions, register
# from product.models import Product, Category

@register(TourDetail)
class TourDetailTranslation(TranslationOptions):
    fields = ('title', 'text',)


@register(Tour)
class TourTranslation(TranslationOptions):
    fields = ('description', )