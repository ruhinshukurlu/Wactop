from django.urls import path, include, re_path
from .views import *

app_name = 'activity'

urlpatterns = [
    path('', ActivityList, name='home'),
    path('<int:pk>', ActivityDetailView, name='detail'),
    path('filter/', ActivityFilter, name='filter')
]