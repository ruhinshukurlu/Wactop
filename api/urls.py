from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework import routers

app_name = 'api'

tour = routers.DefaultRouter()
tour.register('', TourApi)

test = routers.DefaultRouter()
test.register('', TourDetailApi)

urlpatterns = [
    path('tour/', include(tour.urls)),
    path('tourdetail/', include(test.urls)),
]