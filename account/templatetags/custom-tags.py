from django import template
from account.forms import *
from main.models import SocialLink
import datetime
import re, json


register = template.Library()

@register.simple_tag
def login_form():
    return LoginForm


@register.simple_tag
def notifications_count(user):
    print('custom _tag ', Notification.objects.filter(user = user, is_published=True).count())
    return Notification.objects.filter(user = user, is_published=True).count()


@register.simple_tag
def get_social_links():
    return SocialLink.objects.first()

# @register.inclusion_tag('partials/header.html', takes_context=True)
# def notifications_count(context):
#     request = context['request']
#     address = request.session['address']
#     return {'count' : Notification.objects.filter(user = request.user, is_published=True).count()}