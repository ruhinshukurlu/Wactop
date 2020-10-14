from django.db import models
from django.utils.translation import ugettext as _
from account.models import *

class Organizer(models.Model):

    user = models.OneToOneField("account.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name = 'organizer')
    organizer_name = models.CharField(max_length=127, unique=True)
    descriptionaz = models.TextField(blank=True, null=True)
    descriptionen = models.TextField(blank=True, null=True)
    descriptionru = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=127, blank=True, null=True)
    instagram = models.URLField(max_length=127, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    organizer_type = models.ForeignKey('OrganizerType', on_delete=models.SET_NULL, blank=True, null=True,related_name = 'organizer')
    about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=31, blank=True, null=True)
    number2 = models.CharField(max_length=31, blank=True, null=True)
    cover = models.ImageField(upload_to='organizer/cover/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    viewcount = models.IntegerField(default=0)
    
    def __str__ (self):
        return self.organizer_name


class OrganizerType(models.Model):
    type = models.CharField(max_length=31)
    def __str__ (self):
        return self.type

class OrganizerImage(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE,related_name = 'organizer_image')
    image = models.ImageField(upload_to='organizer/image/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.organizer.name


class OrganizerUrl(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE,related_name = 'organizer_url')
    url = models.URLField()
    def __str__ (self):
        return self.organizer.name