from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import login, authenticate
from django.forms import modelformset_factory
from .models import *
from tour.models import *
from training.models import *
from activity.models import *
from django.contrib import messages 
import smtplib
from django.core.mail import send_mail
from Wactop.mail import *




def OrganizerList(request):
    organizer = Organizer.objects.filter(registered=False)
    if request.GET.get('search'):
        context2 = {}
        context2['search'] = request.GET.get('search')
        organizer = Organizer.objects.filter(name__icontains=request.GET.get('search'), registered=False)
        # organizer = Organizer.objects.filter(keyword__icontains=request.GET.get('search'))
    paginator = Paginator(organizer, 2)
    page_request = 'page'
    page = request.GET.get(page_request)
    try:
        eachpage = paginator.page(page)
    except PageNotAnInteger:
        eachpage = paginator.page(1)
    except EmptyPage:
        eachpage = paginator.page(paginator.num_pages)
    
    arr = []
    for i in range(0, eachpage.paginator.num_pages):
        arr.append(i+1)
    context = {
        'organizer': eachpage,
        'page': page_request,
        'paginator': arr,
    }
    if request.GET.get('search'):
        context.update(context2)
    return render(request, 'organizer-list.html', context)


def register(request):
    image_formset = modelformset_factory(OrganizerImage, fields=('image', ), extra=10, form=OrganizerImageRegisterForm)
    
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST or None)
        organizer_form = OrganizerRegisterForm(request.POST, request.FILES)
        image_form = image_formset(request.POST or None, request.FILES or None)

        if user_form.is_valid() and organizer_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            organizer = organizer_form.save(commit=False)
            organizer.user = user
            organizer.registered = True
            organizer.save()
            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.organizer = organizer
                    image.save()
            return redirect('organizer:login')
        else:
            print("___invalid")
    else:
        user_form = UserRegisterForm()
        organizer_form = OrganizerRegisterForm()
        context = {
            'user_form': user_form,
            'organizer_form': organizer_form,
            'image_form': image_formset(queryset=OrganizerImage.objects.none())
        }
        return render(request, 'company-registration.html', context)


def logout_page(request):
    logout(request)
    return redirect('main:home')

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class ProfileEditView(UpdateView):
    model = Organizer
    form_class = ProfileEditForm
    template_name = "edit-profile.html"
    def get_success_url(self):
        return reverse_lazy('organizer:detail', args = (self.kwargs['pk'],))

def OrganizerDetail(request, pk):
    organizer = Organizer.objects.get(pk=pk)
    image = OrganizerImage.objects.filter(organizer=organizer)
    tour = Tour.objects.filter(organizer=organizer)
    training = Training.objects.filter(organizer=organizer)
    activity = Activity.objects.filter(organizer=organizer)
    # image = organizer.organizerimage_set.all()
    context = {
        'organizer': organizer,
        'image': image,
        'tour': tour,
        'training': training,
        'activity': activity
    }
    # return render(request, 'organizer-detail.html', context)
    return render(request, 'company_profile.html', context)


def OrganizerTour(request):
    image_formset = modelformset_factory(TourImage, fields=('image', ), extra=10, form=OrganizerTourImageForm, validate_max=2)
    detail_formset = modelformset_factory(TourDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerTourDetailForm)
    schedule_formset = modelformset_factory(TourSchedule, fields=('image', ), extra=10, form=OrganizerTourScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerTourForm(request.POST or None, request.FILES or None)
        detail_form = detail_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)
        
        if tour_form.is_valid() and detail_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            tour = tour_form.save(commit=False)
            tour.organizer = Organizer.objects.get(user=request.user.id)
            tour.status = 2
            tour.save()
            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.tour = tour
                    image.save()
            for i in detail_form:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()
            for i in schedule_form:
                if i.cleaned_data:
                    schedule = i.save(commit=False)
                    schedule.tour = tour
                    schedule.save()
            # if tour.organizer.email:
            #     message = """
            #         Post saved, you will be notify by email when the post is published
            #         https://www.wactop.com"""
            #     sendemail(tour.organizer.email, message)
            return redirect('tour:home')
        else:
            messages.error(request, "Error")
    else:
        context = {
            'tour_form': OrganizerTourForm,
            'detail_form': detail_formset(queryset=TourDetailEN.objects.none()),
            'image_form': image_formset(queryset=TourImage.objects.none()),
            'schedule_form': schedule_formset(queryset=TourSchedule.objects.none())
        }
        # return render(request, 'organizer-post.html', context)
        return render(request, 'add-tour.html', context)


def OrganizerActivity(request):
    image_formset = modelformset_factory(ActivityImage, fields=('image', ), extra=10, form=OrganizerActivityImageForm)
    detail_formset = modelformset_factory(ActivityDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerActivityDetailForm)
    schedule_formset = modelformset_factory(ActivitySchedule, fields=('image', ), extra=10, form=OrganizerActivityScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerActivityForm(request.POST or None, request.FILES or None)
        detail_form = detail_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)
        if tour_form.is_valid() and detail_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            tour = tour_form.save(commit=False)
            tour.organizer = Organizer.objects.get(user=request.user.id)
            tour.status = 2
            tour.save()
            for i in detail_form:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.activity = tour
                    detail.save()
            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.activity = tour
                    image.save()
            for i in schedule_form:
                if i.cleaned_data:
                    schedule = i.save(commit=False)
                    schedule.activity = tour
                    schedule.save()
            # if tour.organizer.email:
            #     message = """
            #         Post saved, you will be notify by email when the post is published
            #         https://www.wactop.com"""
            #     sendemail(tour.organizer.email, message)
            return redirect('activity:home')
        else:
            messages.error(request, "Error")
    else:
        context = {
            'tour_form': OrganizerActivityForm,
            'detail_form': detail_formset(queryset=ActivityDetailEN.objects.none()),
            'image_form': image_formset(queryset=ActivityImage.objects.none()),
            'schedule_form': schedule_formset(queryset=ActivitySchedule.objects.none())
        }
        return render(request, 'add-activity.html', context)


def OrganizerTraining(request):
    image_formset = modelformset_factory(TrainingImage, fields=('image', ), extra=10, form=OrganizerTrainingImageForm)
    detail_formset = modelformset_factory(TrainingDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerTrainingDetailForm)
    schedule_formset = modelformset_factory(TrainingSchedule, fields=('image', ), extra=10, form=OrganizerTrainingScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerTrainingForm(request.POST or None, request.FILES or None)
        detail_form = detail_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)
        if tour_form.is_valid() and detail_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            tour = tour_form.save(commit=False)
            tour.organizer = Organizer.objects.get(user=request.user.id)
            tour.status = 2
            tour.save()
            for i in detail_form:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.training = tour
                    detail.save()
            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.training = tour
                    image.save()
            for i in schedule_form:
                if i.cleaned_data:
                    schedule = i.save(commit=False)
                    schedule.training = tour
                    schedule.save()
            # if tour.organizer.email:
            #     message = """
            #         Post saved, you will be notify by email when the post is published
            #         https://www.wactop.com"""
            #     sendemail(tour.organizer.email, message)
            return redirect('training:home')
        else:
            messages.error(request, "Error")
    else:
        context = {
            'tour_form': OrganizerTrainingForm,
            'detail_form': detail_formset(queryset=TrainingDetailEN.objects.none()),
            'image_form': image_formset(queryset=TrainingImage.objects.none()),
            'schedule_form': schedule_formset(queryset=TrainingSchedule.objects.none())
        }
        return render(request, 'add-training.html', context)


def test(request):
    return render(request, 'home-page2.html')

