from django.urls import path, include, re_path
from .views import *

app_name = 'organizer'

urlpatterns = [
    path('edit/<int:pk>', OrganizerEditView.as_view(), name='organizer_edit'),

    path('register/', OrganizerRegisterView.as_view(), name='organizer-register'),
    path('profile', OrganizerProfile.as_view(), name='organizer-profile'),
    path('add/tour', OrganizerTour, name='add_tour'),
    path('add/training', OrganizerTraining, name='add_training'),
    path('add/activity', OrganizerActivity, name='add_activity'),
    path("photos", OrganizerPhotoView.as_view(), name="organizer-photos"),
    path("photos/<int:pk>/edit", OrganizerPhotoUpdateView.as_view(), name="organizer-photo-edit"),
    path("photos/<int:pk>/delete", PhotoDeleteView.as_view(), name="photo-delete"),
    path("guides-instructors", GudideInstructorList.as_view(), name="guides-instructors"),
    path("add/guide", GuideCreateView.as_view(), name="add-guide"),
    path("add/instructor", InstructorCreateView.as_view(), name="add-instructor"),

    path("guides/<int:pk>/edit", GuideUpdateView.as_view(), name="guide-edit"),
    path("instructors/<int:pk>/edit", InstructorUpdateView.as_view(), name="instructor-edit"),

    path("guides/<int:pk>/delete", GuideDeleteView.as_view(), name="guide-delete"),
    path("instructors/<int:pk>/delete", InstructorDeleteView.as_view(), name="instructor-delete"),

    path('list/', OrganizerListView.as_view(), name='home'),
    path('<int:pk>', OrganizerDetail, name='detail'),

    path("actions", OrganizerAllActions.as_view(), name="organizer-actions"),

    path("tours/<int:pk>/edit", TourUpdate, name="tour-edit"),
    path("activities/<int:pk>/edit", ActivityUpdate, name="activity-edit"),
    path("trainigs/<int:pk>/edit", TrainingUpdate, name="training-edit"),

    path("tours/<int:pk>/delete", TourDeleteView.as_view(), name="tour-delete"),
    path("activities/<int:pk>/delete", ActivityDeleteView.as_view(), name="activity-delete"),
    path("trainigs/<int:pk>/delete", TrainingDeleteView.as_view(), name="training-delete"), 

    path("tour/<int:pk>/finish", finishTour, name="finish-tour"),
    path("activity/<int:pk>/finish", finishActivity, name="finish-activity"),
    path("training/<int:pk>/finish", finishTraining, name="finish-training"),
    # path("tour/photos", TourImageView.as_view(), name="tour-images"),


]