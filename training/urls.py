from django.urls import path, include, re_path
from .views import *

app_name = 'training'

urlpatterns = [
    path('', TrainingListView.as_view(), name='home'),
    path('<int:pk>', TrainingDetailView, name='detail'),
    path('<int:pk>/comments/', update_items, name='comments'),
    path('filter/', TrainingFilter, name='filter'),
    path('<int:pk>/deny/', TrainingDenyView.as_view(), name='training-deny'),

]