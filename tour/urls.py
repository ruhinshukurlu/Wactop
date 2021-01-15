from django.urls import path, include, re_path
from .views import *

app_name = 'tour'

urlpatterns = [
    path('', TourListView.as_view(), name='home'),
    path('<int:pk>', TourDetailView, name='detail'),
    path('<int:pk>/comments/', update_items, name='comments'),
    path('filter/', TourFilter, name='filter'),
    path('<int:pk>/deny/', TourDenyView.as_view(), name='tour-deny'),

]