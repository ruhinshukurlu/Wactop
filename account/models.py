from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import ugettext_lazy as _
from account.managers import UserManager
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


class Customer(models.Model):
    
    user = models.OneToOneField("account.User", verbose_name=_("Customer"), on_delete=models.CASCADE, primary_key=True, related_name='customer')
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.user.username
    