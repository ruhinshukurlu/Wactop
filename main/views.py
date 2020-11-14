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
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth import authenticate, login
import smtplib
from django.views import View
from django.contrib import messages
from training.views import training_type_list, training_country_list
from tour.views import tour_country_list, tour_type_list
from activity.views import activity_country_list
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


class OrganizerTourFilterView(ListView):
    model = Tour
    context_object_name = 'tours'
    template_name = "tour-list.html"
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["countries"] = tour_country_list
        context['tour_types'] = tour_type_list
        return context

    def get_queryset(self):
        self.organizer = get_object_or_404(Organizer, organizer_name=self.kwargs['organizer_name'])
        if self.request.method == 'GET':
            queryset = Tour.objects.filter(organizer=self.organizer,status=1)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset
        return Tour.objects.filter(organizer=self.organizer,status=1)
       

class OrganizerTrainingFilterView(ListView):
    model = Training
    context_object_name = 'trainings'
    template_name = "training-list.html"
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super(OrganizerTrainingFilterView, self).get_context_data(**kwargs)

        context['countries'] = training_country_list
        context['training_types'] = training_type_list
        return context

    def get_queryset(self):
        self.organizer = get_object_or_404(Organizer, organizer_name=self.kwargs['organizer_name'])
        if self.request.method == 'GET':
            queryset = Training.objects.filter(organizer=self.organizer,status=1)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset  
        return Training.objects.filter(organizer=self.organizer,status=1)
       

class OrganizerActivityFilterView(ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = "activity-list.html"
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["countries"] = activity_country_list
        context['tour_types'] = tour_type_list
        return context


    def get_queryset(self):
        self.organizer = get_object_or_404(Organizer, organizer_name=self.kwargs['organizer_name'])
        if self.request.method == 'GET':
            queryset = Activity.objects.filter(organizer=self.organizer,status=1)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset
        return Activity.objects.filter(organizer=self.organizer,status=1)
       

class TermsView(TemplateView):
    template_name = "terms.html"
  

class PrivacyView(TemplateView):
    template_name = "privacy-policy.html"


class AboutView(TemplateView):
    template_name = "about.html"
