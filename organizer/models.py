from django.db import models
from django.contrib.auth.models import User


class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=127, unique=True)
    descriptionaz = models.TextField(blank=True, null=True)
    descriptionen = models.TextField(blank=True, null=True)
    descriptionru = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=31, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=127, blank=True, null=True)
    instagram = models.CharField(max_length=127, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey('OrganizerType', on_delete=models.SET_NULL, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    number1 = models.CharField(max_length=31, blank=True, null=True)
    number2 = models.CharField(max_length=31, blank=True, null=True)
    avatar = models.ImageField(upload_to='organizer/avatar/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cover = models.ImageField(upload_to='organizer/cover/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    registered = models.BooleanField(default=False)
    viewcount = models.IntegerField(default=0)
    def __str__ (self):
        return self.name


class OrganizerType(models.Model):
    type = models.CharField(max_length=31)
    def __str__ (self):
        return self.type

class OrganizerImage(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='organizer/image/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.organizer.name


class OrganizerUrl(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    url = models.URLField()
    def __str__ (self):
        return self.organizer.name