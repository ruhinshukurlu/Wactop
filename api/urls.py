from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework import routers

app_name = 'api'



urlpatterns = [
    path("tours/", TourList.as_view(), name="tours"),
    path("activities/", ActivityList.as_view(), name="activities"),
    path("trainings/", TrainingList.as_view(), name="trainings")
]