from django.contrib import admin
from main.models import *
# Register your models here.


@admin.register(HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ['slide_image']
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['partner_url' ,'partner_logo']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = [ 'instagram_link', 'facebook_link', 'linkedin_link']   