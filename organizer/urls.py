from django.urls import path, include, re_path
from .views import *

app_name = 'organizer'

urlpatterns = [
    path('', OrganizerList, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register, name='register'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='edit'),
    path('<int:pk>', OrganizerDetail, name='detail'),
    path('add/tour', OrganizerTour, name='addtour'),
    path('add/activity', OrganizerActivity, name='addactivity'),
    path('add/training', OrganizerTraining, name='addtraining'),
    path('test/', test, name='test'),
]