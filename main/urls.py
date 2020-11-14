from django.urls import path, include, re_path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomeView , name='home'),
    path("<organizer_name>/tours", OrganizerTourFilterView.as_view(), name="organizer-tours"),
    path("<organizer_name>/trainings", OrganizerTrainingFilterView.as_view(), name="organizer-trainings"),
    path("<organizer_name>/activities", OrganizerActivityFilterView.as_view(), name="organizer-activities"),
    path("privacies/", PrivacyView.as_view(), name="privacies"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("about/", AboutView.as_view(), name="about")
]