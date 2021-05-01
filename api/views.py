from tour.models import *
from activity.models import *
from training.models import *
from api.serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework
from rest_framework import generics
from rest_framework import filters




class TourList(generics.ListAPIView):
    queryset = Tour.objects.filter(status=1).order_by('-created_at')
    serializer_class = TourSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()

        price_query = self.request.GET.get('price')
        if price_query:
            if price_query == 'high':
                queryset = queryset.order_by('-price')
            elif price_query == 'low':
                queryset = queryset.order_by('price')

        rating_query = self.request.GET.get('rating')
        if rating_query:
            if rating_query == 'high':
                queryset = queryset.order_by('rating')
            elif rating_query == 'low':
                queryset = queryset.order_by('-rating')

        duration_query = self.request.GET.get('duration')
        if duration_query:
            if duration_query == 'long':
                queryset = queryset.order_by('-durationday')
            elif duration_query == 'short':
                queryset = queryset.order_by('durationday')

        countries = self.request.GET.getlist('country[]')
        if countries:
            print(countries)
            queryset = queryset.filter(country__in = countries)

        style_query = self.request.GET.getlist('style[]')
        if style_query:
            queryset = queryset.filter(tour_type__title__in=style_query)

        discount_query = self.request.GET.getlist('discount[]')
        if discount_query:
            queryset = queryset.filter(discount__gte=1)

        return queryset


class ActivityList(generics.ListAPIView):
    queryset = Activity.objects.filter(status=1).order_by('-created_at')
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()

        price_query = self.request.GET.get('price')
        if price_query:
            if price_query == 'high':
                queryset = queryset.order_by('-price')
            elif price_query == 'low':
                queryset = queryset.order_by('price')

        rating_query = self.request.GET.get('rating')
        if rating_query:
            if rating_query == 'high':
                queryset = queryset.order_by('rating')
            elif rating_query == 'low':
                queryset = queryset.order_by('-rating')

        duration_query = self.request.GET.get('duration')
        if duration_query:
            if duration_query == 'long':
                queryset = queryset.order_by('-durationday')
            elif duration_query == 'short':
                queryset = queryset.order_by('durationday')

        countries = self.request.GET.getlist('country[]')
        if countries:
            print(countries)
            queryset = queryset.filter(country__in = countries)

        style_query = self.request.GET.getlist('style[]')
        if style_query:
            queryset = queryset.filter(activity_type__title__in=style_query)

        discount_query = self.request.GET.getlist('discount[]')
        if discount_query:
            queryset = queryset.filter(discount__gte=1)

        return queryset


class TrainingList(generics.ListAPIView):
    queryset = Training.objects.filter(status=1).order_by('-created_at')
    serializer_class = TrainingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()

        price_query = self.request.GET.get('price')
        if price_query:
            if price_query == 'high':
                queryset = queryset.order_by('-price')
            elif price_query == 'low':
                queryset = queryset.order_by('price')

        rating_query = self.request.GET.get('rating')
        if rating_query:
            if rating_query == 'high':
                queryset = queryset.order_by('rating')
            elif rating_query == 'low':
                queryset = queryset.order_by('-rating')

        duration_query = self.request.GET.get('duration')
        if duration_query:
            if duration_query == 'long':
                queryset = queryset.order_by('-durationday')
            elif duration_query == 'short':
                queryset = queryset.order_by('durationday')

        countries = self.request.GET.getlist('country[]')
        if countries:
            print(countries)
            queryset = queryset.filter(country__in = countries)

        style_query = self.request.GET.getlist('style[]')
        if style_query:
            queryset = queryset.filter(training_type__title__in=style_query)

        discount_query = self.request.GET.getlist('discount[]')
        if discount_query:
            queryset = queryset.filter(discount__gte=1)

        return queryset


