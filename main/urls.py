from django.urls import path, include, re_path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('test', test)
]