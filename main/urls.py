from django.urls import path, include, re_path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView , name='home'),
    path("<organizer_name>/tour", OrganizerTourFilterView.as_view(), name="organizer-tours"),
    path("<organizer_name>/training", OrganizerTrainingFilterView.as_view(), name="organizer-trainings"),
    path("<organizer_name>/activity", OrganizerActivityFilterView.as_view(), name="organizer-activities"),

]