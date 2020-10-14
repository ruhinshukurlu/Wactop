from django.urls import path, include, re_path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView , name='home'),
]