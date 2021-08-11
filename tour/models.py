from django.db import models
from organizer.models import *
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
import smtplib
from django.core.mail import send_mail
from Wactop.mail import *
from django.utils.translation import ugettext as _
from slugify import slugify
from ckeditor.fields import RichTextField

status_choices = [(1, 'publish'), (2, 'draft'), (3, 'past'), (4, 'deny')]


class TourType(models.Model):
    title = models.CharField(max_length=31)
    def __str__ (self):
        return self.title

class Type(models.Model):
    type = models.CharField(max_length=31)
    def __str__ (self):
        return self.type


class Tour(models.Model):

    CURRENCIES = [
        ('AZN', 'AZN'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('TRY', 'TRY'),
        ('RUB','RUB')
    ]

    organizer = models.ForeignKey(Organizer, on_delete=models.SET_NULL, blank=True, null=True, related_name='tour')
    title = models.CharField(max_length=63)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    tour_type = models.ForeignKey(TourType, on_delete=models.CASCADE, related_name='tour')
    country = models.CharField(max_length=31, default='Azerbaijan')
    city = models.CharField(max_length=31, null=True, blank=True)
    address = models.CharField(max_length=63, null=True, blank=True)
    price = models.IntegerField()
    pricefor = models.IntegerField(default=1)
    currency = models.CharField(max_length=31, default='AZN', choices = CURRENCIES)
    discount = models.IntegerField(blank=True, null=True)
    distance = models.CharField(max_length=31, blank=True, null=True)
    durationday = models.IntegerField(blank=True, null=True)
    durationnight = models.IntegerField(blank=True, null=True)

    datefrom = models.DateField(blank=True, null=True)
    dateto = models.DateField(blank=True, null=True)

    viewcount = models.IntegerField(default=0, blank=True, null=True)
    avatar = models.ImageField(upload_to='tour/avatar/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    cover = models.ImageField(upload_to='tour/cover/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    guide = models.CharField(max_length=31, blank=True, null=True)
    status = models.IntegerField(choices=status_choices, default=1)
    rating = models.IntegerField(_("Rating"), blank=True, null=True, default=0)
    activated = models.BooleanField(_("Activated"), default  = False)

    slug = models.SlugField(_("Slug"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True )

    map_link = models.URLField(_("Map Link"), max_length=300, blank=True, null=True)

    def __str__ (self):
        return self.title

    old_status = None
    def __init__(self, *args, **kwargs):
        super(Tour, self).__init__(*args, **kwargs)
        self.old_status = self.status

    def discount_price(self):
        new_price = self.price - (self.price * self.discount) // 100
        return new_price

    def discount_price_api(self):
        if self.discount:
            new_price = self.price - (self.price * self.discount) // 100
        else:
            new_price = 0
        return new_price

    def get_duration_day(self):
        if self.datefrom and self.dateto:
            start_date = self.datefrom
            end_date = self.dateto
            return (end_date-start_date).days
        else:
            return False

    def get_duration_day_api(self):
        duration = ''
        if self.datefrom and self.dateto:
            start_date = self.datefrom
            end_date = self.dateto
            duration = f'{(end_date-start_date).days} days'
        else:
            duration = 'Always'

        return duration

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Tour, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.old_status != self.status:
    #         if self.status == 1:
    #             if self.organizer.email:
    #                 message = """
    #                     Your post has been verificiated
    #                     Visit https://www.wactop.com"""
    #                 sendemail(self.organizer.email, message)
    #     super(Tour, self).save(*args, **kwargs)



class TourDetail(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_detail')
    title = models.CharField(max_length=31)
    text = RichTextField(blank = True)

    def __str__ (self):
        return self.tour.title + ": " + self.title


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_image')
    image = models.ImageField(upload_to='tour/image/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.tour.title

class TourSchedule(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_schedule')
    schedule_image = models.ImageField(upload_to='tour/schedule/', height_field=None, width_field=None, max_length=None)
    def __str__ (self):
        return self.tour.title

class TourUrl(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_url')
    url = models.URLField()
    def __str__ (self):
        return self.tour.title



class TourComment(models.Model):
    message = models.TextField(_("Text"))
    commented_at = models.DateField(_("Commented at"), auto_now_add=True)
    rating = models.IntegerField(_("Rating"), blank=True, null=True)

    comment_reply = models.ForeignKey("self", verbose_name=_("Comment"), on_delete=models.CASCADE, blank=True, null = True, related_name='replies')
    tour = models.ForeignKey("tour.Tour", verbose_name=_("Tour"), on_delete=models.CASCADE, blank=True, null=True, related_name='tour_comment')
    user = models.ForeignKey("account.User", verbose_name=_("User"), on_delete=models.CASCADE, blank=True, null=True, related_name='tour_comment')

    def __str__ (self):
        return self.message


class TourDeny(models.Model):
    # informations
    message = models.TextField(_("Text"))

    # relations
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='deny')

    # moderations
    created_at = models.DateField(_("Commented at"), auto_now_add=True)
    updated_at = models.DateField(_("Commented at"), auto_now=True)


    class Meta:
        verbose_name = _("TourDeny")
        verbose_name_plural = _("TourDenies")

    def __str__(self):
        return str(self.tour)

