from django.urls import path, include, re_path
from .views import *

app_name = 'tour'

urlpatterns = [
    path('', TourList, name='home'),
    path('<int:pk>', TourDetailView, name='detail'),
    path('filter/', TourFilter, name='filter')
]