from django.db import models
from organizer.models import *
from tour.models import status_choices, Type, TourType
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext as _

import smtplib
from django.core.mail import send_mail
from Wactop.mail import *



class Training(models.Model):

    CURRENCIES = [
        ('AZN', 'AZN'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('TRY', 'TRY'),
        ('RUB','RUB')
    ]
 

    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, blank=True, null=True, related_name='training')
    title = models.CharField(max_length=63)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    descriptionaz = models.TextField(blank=True, null=True)
    descriptionen = models.TextField(blank=True, null=True)
    descriptionru = models.TextField(blank=True, null=True)
    training_type = models.ForeignKey(TourType, on_delete=models.CASCADE, related_name='training')

    country = models.CharField(max_length=31, default='Azerbaijan')
    city = models.CharField(max_length=31, null=True, blank=True)
    address = models.CharField(max_length=63, null=True, blank=True)
    price = models.IntegerField()
    pricefor = models.IntegerField(default=1)
    currency = models.CharField(max_length=31, choices = CURRENCIES, default='AZN')
    discount = models.IntegerField(blank=True, null=True)
    distance = models.CharField(max_length=31, blank=True, null=True)
    durationday = models.IntegerField(blank=True, null=True)
    durationnight = models.IntegerField(blank=True, null=True)
    datefrom = models.DateField(blank=True, null=True)
    dateto = models.DateField(blank=True, null=True)
    viewcount = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='training/avatar/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cover = models.ImageField(upload_to='training/cover/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    trainer = models.CharField(max_length=31, blank=True, null=True)
    availabledays = models.CharField(max_length=31, blank=True, null=True)
    status = models.IntegerField(choices=status_choices, default=1)

    start_hour = models.TimeField(_("Start Hour"))
    finish_hour = models.TimeField(_("Finish Hour"))

    map_link = models.URLField(_("Map Link"), max_length=300, blank=True, null=True)
    
    old_status = None

    def __init__(self, *args, **kwargs):
        super(Training, self).__init__(*args, **kwargs)
        self.old_status = self.status
    # def save(self, *args, **kwargs):
    #     if self.old_status != self.status:
    #         if self.status == 1:
    #             if self.organizer.email:
    #                 message = """
    #                     Your post has been verificiated
    #                     Visit https://www.wactop.com"""
    #                 sendemail(self.organizer.email, message)
    #     super(Training, self).save(*args, **kwargs)
    def __str__ (self):
        return self.title

class TrainingDetailAZ(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_detail_az')
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "AZ" + self.training.title + ": " + self.title

class TrainingDetailEN(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_detail_en')
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "EN" + self.training.title + ": " + self.title

class TrainingDetailRU(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_detail_ru')
    title = models.CharField(max_length=31)
    text = models.TextField()
    def __str__ (self):
        return "RU" + self.training.title + ": " + self.title

class TrainingImage(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_image')
    image = models.ImageField(upload_to='training/image/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.training.title

class TrainingSchedule(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_schedule')
    image = models.ImageField(upload_to='training/schedule/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.training.title

class TrainingUrl(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='training_url')
    url = models.URLField()

    def __str__ (self):
        return self.training.title


class Comment(models.Model):
    message = models.TextField(_("Text"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    rating = models.IntegerField(_("Rating"), blank=True, null=True)

    comment_reply = models.ForeignKey("self", verbose_name=_("Comment"), on_delete=models.CASCADE, blank=True, null = True, related_name='replies')
    training = models.ForeignKey("training.Training", verbose_name=_("Training"), on_delete=models.CASCADE, blank=True, null=True, related_name='comment')
    user = models.ForeignKey("account.User", verbose_name=_("User"), on_delete=models.CASCADE, blank=True, null=True, related_name='comment')
   
    def __str__ (self):
        return self.message