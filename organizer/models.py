from django.db import models
from django.utils.translation import ugettext as _
from account.models import *


class Organizer(models.Model):

    user = models.OneToOneField("account.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name = 'organizer')
    email = models.EmailField(_("Email"), max_length=254)
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
    contact_number_1 = models.CharField(max_length=31, blank=True, null=True)
    contact_number_2 = models.CharField(max_length=31, blank=True, null=True)
    profile_photo = models.ImageField(_("organizer/profile-photo"), upload_to=None, height_field=None, width_field=None, max_length=None)
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
        return self.organizer.organizer_name


class OrganizerUrl(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE,related_name = 'organizer_url')
    url = models.URLField()
    def __str__ (self):
        return self.organizer.name


EPERIENCE_CHOICES = [
    ('1 year', '1 Year'),
    ('2 year', '2 Year'),
    ('3 year', '3 Year'),
    ('4 year', '4 Year'),
    ('5+ year', '5+ Year'),
]


class Guide(models.Model):

    organizer = models.ForeignKey(Organizer, verbose_name=_("Organizer"), on_delete=models.CASCADE, related_name = 'guide')
    name = models.CharField(_("Name"), max_length=50)
    surname = models.CharField(_("Surname"), max_length=50)
    experience =  models.CharField(_("Experience"), max_length=50, choices = EPERIENCE_CHOICES)
    certification = models.CharField(_("Certification"), max_length=50)

    def __str__(self):
        return self.name


class Instructor(models.Model):

    organizer = models.ForeignKey(Organizer, verbose_name=_("Organizer"), on_delete=models.CASCADE, related_name = 'instructor')
    name = models.CharField(_("Name"), max_length=50)
    surname = models.CharField(_("Surname"), max_length=50)
    experience =  models.CharField(_("Experience"), max_length=50, choices = EPERIENCE_CHOICES)
    certification = models.CharField(_("Certification"), max_length=50)

    def __str__(self):
        return self.name