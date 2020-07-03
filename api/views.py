from django.shortcuts import render
from rest_framework import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from tour.models import Tour
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated


class TourApi(ReadOnlyModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    def get_queryset(self):
        country = self.request.GET.get('country')
        if country:
            return Tour.objects.filter(country__icontains=country)
        low = self.request.GET.get('low')
        if low:
            return Tour.objects.all().order_by('price')
        high = self.request.GET.get('high')
        if high:
            return Tour.objects.all().order_by('-price')
        return super().get_queryset()

class TourDetailApi(ReadOnlyModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer
    def get_queryset(self):
        pk = self.request.GET.get('id')
        tour = Tour.objects.filter(pk=pk)
        az = TourDetailAZ.objects.filter(tour=tour)
        en = TourDetailEN.objects.filter(tour=tour)
        ru = TourDetailEN.objects.filter(tour=tour)
        
        if tour:
            return tour
        return super().get_queryset()