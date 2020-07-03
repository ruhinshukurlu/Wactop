from rest_framework import serializers
from tour.models import *


class TourSerializer(serializers.ModelSerializer):
    organizer_name = serializers.CharField(source='organizer.name')
    class Meta:
        model = Tour
        fields = '__all__'


class TourDetailSerializer(serializers.ModelSerializer):
    organizer_name = serializers.CharField(source='organizer.name')
    class Meta:
        model = Tour
        fields = '__all__'