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

    path('list', OrganizerListView.as_view(), name='home'),
    path('<int:pk>', OrganizerDetail, name='detail'),

    path("actions", OrganizerAllActions.as_view(), name="organizer-actions"),

    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', logout_page, name='logout'),
    # path('register/', register, name='register'),
    # path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit'),
    # path('add/tour', OrganizerTour, name='addtour'),
    # path('add/activity', OrganizerActivity, name='addactivity'),
    # path('add/training', OrganizerTraining, name='addtraining'),
    # path('test/', test, name='test'),
    # path('', OrganizerList, name='home'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', logout_page, name='logout'),
    # path('register/', register, name='register'),
    # path('<int:pk>', OrganizerDetail, name='detail'),
    # path('<int:pk>/images', organizer_image_list, name = 'organizer_image_list'),
    # path('add/tour', OrganizerTour, name='addtour'),
    # path('test/', test, name='test'),

]