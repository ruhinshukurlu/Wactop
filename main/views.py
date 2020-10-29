from django.shortcuts import render, redirect
from django.http import HttpResponse
from tour.models import *
from account.forms import *
from activity.models import Activity
from training.models import Training
from organizer.models import Organizer
from django.shortcuts import get_object_or_404
import smtplib
from Wactop.mail import *
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth import authenticate, login
import smtplib
from django.views import View
from django.contrib import messages

# sendemail("kamil129@inbox.ru", "test2")


def HomeView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:

            if user.is_active:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('main:home')
        else:
            messages.error(request,'Email or password is not correct')
            return redirect('main:home')

    else:
        form = LoginForm()
        tourcount = Tour.objects.filter(status=1).count()
        activitycount = Activity.objects.filter(status=1).count()
        trainingcount = Training.objects.filter(status=1).count()
        organizercount = Organizer.objects.all().count() 
    context = {
        'tourcount': tourcount,
        'activitycount': activitycount,
        'trainingcount': trainingcount,
        'organizercount': organizercount,
        # 'pk': pk,
        'form': form
    }
    return render(request, 'home-page.html', context)


