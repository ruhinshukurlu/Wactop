from django.shortcuts import render
from django.http import HttpResponse
from tour.models import *
from activity.models import Activity
from training.models import Training
from organizer.models import Organizer
from django.shortcuts import get_object_or_404
import smtplib
from Wactop.mail import *


import smtplib
# sendemail("kamil129@inbox.ru", "test2")


def home(request):
    tourcount = Tour.objects.filter(status=1).count()
    activitycount = Activity.objects.filter(status=1).count()
    trainingcount = Training.objects.filter(status=1).count()
    organizercount = Organizer.objects.filter(registered=False).count()
    if request.user.is_authenticated and not request.user.is_superuser:
        pk = Organizer.objects.get(user=request.user.id).id
    else:
        pk = 1
    context = {
        'tourcount': tourcount,
        'activitycount': activitycount,
        'trainingcount': trainingcount,
        'organizercount': organizercount,
        'pk': pk
    }
    return render(request, 'home-page.html', context)

def test(request):
    tour = Tour.objects.get(pk=8)
    detail = TourDetailEN.objects.filter(tour=tour)
    context = {
        'detail': detail
    }
    return render(request, 'test2.html', context)