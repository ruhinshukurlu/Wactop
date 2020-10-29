from django.urls import path, include, re_path
from .views import *

app_name = 'training'

urlpatterns = [
    path('', TrainingListView.as_view(), name='home'),
    path('<int:pk>', TrainingDetailView, name='detail'),
    path('filter/', TrainingFilter, name='filter')
]