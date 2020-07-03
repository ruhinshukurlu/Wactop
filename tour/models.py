from django.db import models
from organizer.models import *
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
import smtplib
from django.core.mail import send_mail
from Wactop.mail import *

status_choices = [(1, 'publish'), (2, 'draft'), (3, 'past')]

class Type(models.Model):
    type = models.CharField(max_length=31)
    def __str__ (self):
        return self.type



class Tour(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=63)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    descriptionaz = models.TextField(blank=True, null=True)
    descriptionen = models.TextField(blank=True, null=True)
    descriptionru = models.TextField(blank=True, null=True)
    # type = MultiSelectField(choices=type_choices, max_choices=3, max_length=3, blank=True, null=True)
    type = models.ManyToManyField(Type, verbose_name=("type"), related_name="tour", blank=True)
    country = models.CharField(max_length=31, default='Azerbaijan')
    city = models.CharField(max_length=31, null=True, blank=True)
    adress = models.CharField(max_length=63, null=True, blank=True)
    price = models.IntegerField()
    pricefor = models.IntegerField(default=1)
    currency = models.CharField(max_length=31, default='AZN')
    discount = models.IntegerField(blank=True, null=True)
    distance = models.CharField(max_length=31, blank=True, null=True)
    durationday = models.IntegerField(blank=True, null=True)
    durationnight = models.IntegerField(blank=True, null=True)
    datefrom = models.DateField()
    dateto = models.DateField(blank=True, null=True)
    viewcount = models.IntegerField(default=0, blank=True, null=True)
    avatar = models.ImageField(upload_to='tour/avatar/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cover = models.ImageField(upload_to='tour/cover/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    guide = models.CharField(max_length=31, blank=True, null=True)
    status = models.IntegerField(choices=status_choices, default=1)

    def __str__ (self):
        return self.title
    
    old_status = None
    def __init__(self, *args, **kwargs):
        super(Tour, self).__init__(*args, **kwargs)
        self.old_status = self.status

    # def save(self, *args, **kwargs):
    #     if self.old_status != self.status:
    #         if self.status == 1:
    #             if self.organizer.email:
    #                 message = """
    #                     Your post has been verificiated
    #                     Visit https://www.wactop.com"""
    #                 sendemail(self.organizer.email, message)
    #     super(Tour, self).save(*args, **kwargs)

class TourDetailAZ(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "AZ" + self.tour.title + ": " + self.title

class TourDetailEN(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "EN" + self.tour.title + ": " + self.title

class TourDetailRU(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "RU" + self.tour.title + ": " + self.title

class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tour/image/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.tour.title

class TourSchedule(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tour/schedule/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.tour.title

class TourUrl(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    url = models.URLField()
    def __str__ (self):
        return self.tour.title