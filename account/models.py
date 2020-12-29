from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import ugettext_lazy as _
from account.managers import UserManager
from django.core.mail import send_mail, EmailMessage
from Wactop.settings import EMAIL_HOST_USER
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

from django.http import JsonResponse
# Create your models here.

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_organizer = models.BooleanField(default=False)
    
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    username = models.CharField(_('Username'), unique=True, max_length=30, blank=True)
    profile_img = models.ImageField(_("Profile image"),upload_to='profile-pictures/', null=True, blank=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


    # def save(self, *args, **kwargs):
    #     if self.is_active:
    #         send_mail('salam', 'olsun', EMAIL_HOST_USER, [self.email] )


@receiver(post_save,sender=User)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    if instance.is_active:
        email = instance.email
        html_content = "you Organizer is activated by admin"
        send_mail('Hello', html_content ,  EMAIL_HOST_USER, [email])

class Customer(models.Model):
    
    user = models.OneToOneField("account.User", verbose_name=_("Customer"), on_delete=models.CASCADE, primary_key=True, related_name='customer')
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.user.username
    