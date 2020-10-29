from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
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
from account.forms import *


class OrganizerRegisterView(CreateView):
    model = User
    form_class = OrganizerRegisterForm
    template_name = 'organizer-register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'organizer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
       
        return redirect('main:home')


class OrganizerProfile(TemplateView):
    template_name = 'organizer-profile.html'


class OrganizerListView(ListView):
    model = Organizer
    context_object_name = 'organizers'
    template_name = "organizer-list.html"



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


# def register(request):
#     image_formset = modelformset_factory(OrganizerImage, fields=('image', ), extra=10, form=OrganizerImageRegisterForm)
    
#     if request.method == 'POST':
#         user_form = UserRegisterForm(request.POST or None)
#         organizer_form = OrganizerRegisterForm(request.POST, request.FILES)
#         image_form = image_formset(request.POST or None, request.FILES or None)

#         if user_form.is_valid() and organizer_form.is_valid() and image_form.is_valid():
#             user = user_form.save()
#             organizer = organizer_form.save(commit=False)
#             organizer.user = user
#             organizer.registered = True
#             organizer.save()
#             for i in image_form:
#                 if i.cleaned_data:
#                     image = i.save(commit=False)
#                     image.organizer = organizer
#                     image.save()
#             return redirect('organizer:login')
#         else:
#             print("___invalid")
#     else:
#         user_form = UserRegisterForm()
#         organizer_form = OrganizerRegisterForm()
#         context = {
#             'user_form': user_form,
#             'organizer_form': organizer_form,
#             'image_form': image_formset(queryset=OrganizerImage.objects.none())
#         }
#         return render(request, 'company-registration.html', context)


# def logout_page(request):
#     logout(request)
#     return redirect('main:home')


# class CustomLoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'login.html'


class OrganizerEditView(UpdateView):
    model = Organizer
    form_class = OrganizerEditForm
    context_object_name = 'organizer'
    template_name = "organizer-edit.html"

    def get_success_url(self):
        return reverse_lazy('organizer:detail', args = (self.kwargs['pk'],))
    

class OrganizerPhotoView(CreateView):
    model = OrganizerImage
    form_class = OrganizerPhotoForm
    template_name = 'organizer-photos.html'
    success_url = reverse_lazy('organizer:organizer-photos')

    def form_valid(self, form):
        form.instance.organizer = self.request.user.organizer
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = OrganizerImage.objects.filter(organizer=self.request.user.organizer)
        
        return context

class OrganizerPhotoUpdateView(UpdateView):
    model = OrganizerImage
    form_class = OrganizerPhotoEditForm
    context_object_name = 'photo'
    template_name = "org-photo-edit.html"

    def get_success_url(self):
        return reverse_lazy('organizer:organizer-photos')


class PhotoDeleteView(DeleteView):
    model = OrganizerImage
    template_name = "org-photo-edit.html"

    def get_success_url(self):
        return reverse_lazy('organizer:organizer-photos')


class GudideInstructorList(ListView):
    model = Guide
    context_object_name = 'guides'
    template_name = 'guides-instructors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["instructors"] = Instructor.objects.filter(organizer = self.request.user.organizer)
        return context

    def get_queryset(self):
        return Guide.objects.filter(organizer = self.request.user.organizer)


class GuideCreateView(CreateView):
    model = Guide
    form_class = GuideForm
    template_name = "add-guide-instructor.html"

    def form_valid(self, form):
        form.instance.organizer = self.request.user.organizer
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('organizer:guides-instructors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["worker"] = 'Guide'
        return context
    

class GuideUpdateView(UpdateView):
    model = Guide
    form_class = GuideForm
    context_object_name = 'guide'
    template_name = "add-guide-instructor.html"

class GuideDeleteView(DeleteView):
    model = Guide

    def get_success_url(self):
        return reverse_lazy('organizer:guides-instructors')



class InstructorCreateView(CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = "add-guide-instructor.html"

    def form_valid(self, form):
        form.instance.organizer = self.request.user.organizer
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('organizer:guides-instructors')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["worker"] = 'Instructor'
        return context


class InstructorUpdateView(UpdateView):
    model = Instructor
    form_class = InstructorForm
    context_object_name = 'instructor'
    template_name = "add-guide-instructor.html"

    def get_success_url(self):
        return reverse_lazy('organizer:guides-instructors')


class InstructorDeleteView(DeleteView):
    model = Instructor

    def get_success_url(self):
        return reverse_lazy('organizer:guides-instructors')


class OrganizerAllActions(ListView):
    model = Tour
    template_name = 'organizer-history.html'
    context_object_name = 'tours'

    def get_queryset(self):
        return super().get_queryset().filter(organizer=self.request.user.organizer)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activities"] = Activity.objects.filter(organizer=self.request.user.organizer)
        context['trainings'] = Training.objects.filter(organizer=self.request.user.organizer)
        return context
    


def OrganizerDetail(request, pk):
    organizer = Organizer.objects.get(pk=pk)
    images = OrganizerImage.objects.filter(organizer=organizer)
    tours = Tour.objects.filter(organizer=organizer)
    training = Training.objects.filter(organizer=organizer)
    activity = Activity.objects.filter(organizer=organizer)

    guides = Guide.objects.filter(organizer=organizer)
    instructors = Instructor.objects.filter(organizer=organizer)

    # image = organizer.organizerimage_set.all()
    context = {
        'organizer': organizer,
        'images': images,
        'tours': tours,
        'training': training,
        'activity': activity,
        'guides' : guides,
        'instructors' : instructors
    }
    # return render(request, 'organizer-detail.html', context)
    return render(request, 'company-profile.html', context)

def organizer_image_list(request, pk):
    organizer = Organizer.objects.get(pk=pk)
    image = OrganizerImage.objects.filter(organizer=organizer)

    context = {
        'organizer': organizer,
        'image_list': image,
    }
    return render(request, 'image-list.html', context)



def OrganizerTour(request):
    # print(Organizer.objects.filter(user=request.user))
    image_formset = modelformset_factory(TourImage, fields=('image', ), extra=10, form=OrganizerTourImageForm, validate_max=2)
    detail_formset = modelformset_factory(TourDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerTourDetailForm)
    schedule_formset = modelformset_factory(TourSchedule, fields=('image', ), extra=10, form=OrganizerTourScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerTourForm(request.POST or None, request.FILES or None)
        detail_form = detail_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)
        print(tour_form.errors, image_form.errors, schedule_form.errors)
        if tour_form.is_valid() and detail_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            print('oookkkkk')
            
            tour = tour_form.save(commit=False)
            tour.organizer = request.user.organizer
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
            tour.organizer = request.user.organizer

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


