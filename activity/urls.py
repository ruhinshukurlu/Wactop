from django.urls import path, include, re_path
from .views import *

app_name = 'activity'

urlpatterns = [
    path('', ActivityListView.as_view(), name='home'),
    # path("high/", ActivityHighFilterListView.as_view(), name="high-filter"),
    # path("low/", ActivityLowFilterListView.as_view(), name="low-filter"),
    path('<int:pk>', ActivityDetailView, name='detail'),
    path('filter/', ActivityFilter, name='filter')
]