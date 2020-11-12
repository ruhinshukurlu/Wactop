from django.urls import path, include, re_path
from .views import *

app_name = 'activity'

urlpatterns = [
    path('', ActivityListView.as_view(), name='home'),
    path('<int:pk>', ActivityDetailView, name='detail'),
    path('<int:pk>/comments/', update_items, name='comments'),
    path('filter/', ActivityFilter, name='filter')
]