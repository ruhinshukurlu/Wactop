from django.db import models
from django.utils.translation import ugettext as _



class HomeSlide(models.Model):

    slide_image = models.ImageField(_("Slide Image"), upload_to='slide-images', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("HomeSlide")
        verbose_name_plural = _("HomeSlides")

    def __str__(self):
        return str(self.slide_image)


class Partner(models.Model):
    partner_url = models.URLField(_("Partner Link"), max_length=300, blank=True, null=True)
    partner_logo = models.ImageField(_("Partner Logo"), upload_to='partner-images', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")

    def __str__(self):
        return str(self.partner_logo)


class SocialLink(models.Model):
    instagram_link = models.URLField(_("Instagram Link"), max_length=300, blank=True, null=True)
    facebook_link = models.URLField(_("Facebook Link"), max_length=300, blank=True, null=True)
    linkedin_link = models.URLField(_("LinkedIn Link"), max_length=300, blank=True, null=True)


    class Meta:
        verbose_name = _("SocialLink")
        verbose_name_plural = _("SocialLinks")

    def __str__(self):
        return str(self.instagram_link)