from rest_framework import serializers
from tour.models import *
from activity.models import *
from training.models import *
from organizer.models import *


class CustomCharField(serializers.CharField):

    def __init__(self, repr_length, **kwargs):
        self.repr_length = repr_length
        super(CustomCharField, self).__init__(**kwargs)

    def to_representation(self, value):
        return super(CustomCharField, self).to_representation(value)[:self.repr_length].capitalize()


class TourCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourComment
        fields = '__all__'


class ActivityCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityComment
        fields = '__all__'


class TrainingCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    organizer_name = serializers.CharField(source='organizer.organizer_name')
    tour_type = serializers.CharField(source='tour_type.title')
    comment_list = TourCommentSerializer(source='tour_comment', many=True)
    new_price = serializers.IntegerField(source = 'discount_price_api')
    durationday = serializers.CharField(source = 'get_duration_day_api')


    class Meta:
        model = Tour
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    organizer_name = CustomCharField(source='organizer.organizer_name', repr_length=20)
    activity_type = serializers.CharField(source='activity_type.title')
    comment_list = ActivityCommentSerializer(source='activity_comment', many=True)
    new_price = serializers.IntegerField(source = 'discount_price_api')
    durationday = serializers.CharField(source = 'get_duration_day_api')


    class Meta:
        model = Activity
        fields = '__all__'


class TrainingSerializer(serializers.ModelSerializer):
    organizer_name = CustomCharField(source='organizer.organizer_name', repr_length=20)
    training_type = serializers.CharField(source='training_type.title')
    comment_list = TrainingCommentSerializer(source='comment', many=True)
    new_price = serializers.IntegerField(source = 'discount_price_api')
    durationday = serializers.CharField(source = 'get_duration_day_api')


    class Meta:
        model = Training
        fields = '__all__'