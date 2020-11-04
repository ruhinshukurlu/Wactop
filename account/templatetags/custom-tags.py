from django import template
from account.forms import *
import datetime
import re


register = template.Library()

@register.simple_tag
def login_form():
    return LoginForm
