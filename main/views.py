from django.shortcuts import render, redirect
from django.http import HttpResponse
from tour.models import *
from account.forms import *
from activity.models import Activity
from training.models import Training
from organizer.models import Organizer
from django.shortcuts import get_object_or_404
from Wactop.mail import *
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages
from main.models import *
from organizer.forms import *

from django.contrib import messages
import smtplib
from django.core.mail import send_mail, EmailMultiAlternatives
from Wactop.mail import *
from account.forms import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def HomeView(request):
    slide_images = HomeSlide.objects.all()
    partners = Partner.objects.all()
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
        tours = Tour.objects.filter(status=1).order_by('-created_at')[:4]
        activities = Activity.objects.filter(status=1).order_by('-created_at')[:4]
        trainings = Training.objects.filter(status=1).order_by('-created_at')[:4]
    context = {
        'tours': tours,
        'activities': activities,
        'trainings': trainings,
        'form': form,
        'slide_images': slide_images,
        'partners': partners,
    }
    return render(request, 'home-page.html', context)


class OrganizerTourFilterView(ListView):
    model = Tour
    context_object_name = 'tours'
    template_name = "tour-list-no-filter.html"
    paginate_by = 16

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
    context_object_name = 'tours'
    template_name = "tour-list-no-filter.html"
    paginate_by = 16


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
    context_object_name = 'tours'
    template_name = "tour-list-no-filter.html"
    paginate_by = 16


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

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact.html"

    def form_valid(self, form):
        form.save()
        subject = 'New user contacted'
        text_content = 'New user contacted'
        html_content = f"<p>First name : {form.cleaned_data['first_name']}</p><p>Last name : {form.cleaned_data['last_name']}</p><p>Email : {form.cleaned_data['email']}</p><p>Phone number : {form.cleaned_data['phone_number']}</p><p>Message : {form.cleaned_data['message']}</p>"
        sendMail(subject,text_content,html_content)

        return redirect('main:home')