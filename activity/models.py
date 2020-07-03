from django.db import models
from organizer.models import *
from tour.models import status_choices, Type
from multiselectfield import MultiSelectField
import smtplib
from django.core.mail import send_mail
from Wactop.mail import *


class Activity(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=63)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    descriptionaz = models.TextField(blank=True, null=True)
    descriptionen = models.TextField(blank=True, null=True)
    descriptionru = models.TextField(blank=True, null=True)
    type = models.ManyToManyField(Type, verbose_name=("type"), related_name="activity", blank=True)
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
    datefrom = models.DateField(blank=True, null=True)
    dateto = models.DateField(blank=True, null=True)
    viewcount = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='activity/avatar/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cover = models.ImageField(upload_to='activity/cover/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    guide = models.CharField(max_length=31, blank=True, null=True)
    availabledays = models.CharField(max_length=31, blank=True, null=True)
    status = models.IntegerField(choices=status_choices, default=1)
    old_status = None
    def __init__(self, *args, **kwargs):
        super(Activity, self).__init__(*args, **kwargs)
        self.old_status = self.status
    # def save(self, *args, **kwargs):
    #     if self.old_status != self.status:
    #         if self.status == 1:
    #             if self.organizer.email:
    #                 message = """
    #                     Your post has been verificiated
    #                     Visit https://www.wactop.com"""
    #                 sendemail(self.organizer.email, message)
    #     super(Activity, self).save(*args, **kwargs)
    def __str__ (self):
        return self.title

class ActivityDetailAZ(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "AZ" + self.activity.title + ": " + self.title

class ActivityDetailEN(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "EN" + self.activity.title + ": " + self.title

class ActivityDetailRU(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "RU" + self.activity.title + ": " + self.title

class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='activity/image/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.activity.title

class ActivitySchedule(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='activity/schedule/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.activity.title

class ActivityUrl(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    url = models.URLField()
    def __str__ (self):
        return self.activity.title