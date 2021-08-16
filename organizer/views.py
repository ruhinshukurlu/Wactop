from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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
from django.core.mail import send_mail, EmailMultiAlternatives
from Wactop.mail import *
from account.forms import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from organizer.mixin import FormsetMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from organizer.mixin import NotificationMixin



class OrganizerRegisterView(CreateView):
    model = User
    form_class = OrganizerRegisterForm
    template_name = 'organizer-register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'organizer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        subject = 'New organizer registered'
        data =[
            form.cleaned_data['organizer_name'],
            form.cleaned_data['email'],
            form.cleaned_data['description'],
            form.cleaned_data['about'],
            form.cleaned_data['address'],
            form.cleaned_data['website'],
            form.cleaned_data['facebook'],
            form.cleaned_data['instagram'],
            form.cleaned_data['contact_number1'],
            form.cleaned_data['contact_number2'],
            form.cleaned_data['cover_image'],
            form.cleaned_data['profile_image']
        ]
        html_content = render_to_string('partials/mail_template.html', {'organzer_data':data}) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

        # html_content = f"<p>Organizer name : {form.cleaned_data['organizer_name']}</p><p>Organizer email : {form.cleaned_data['email']}</p><p>Organizer description : {form.cleaned_data['description']}</p><p>About Organizer : {form.cleaned_data['about']}</p><p>Organizer address : {form.cleaned_data['address']}</p><p>Organizer website : {form.cleaned_data['website']}</p><p>Organizer facebook : {form.cleaned_data['facebook']}</p><p>Organizer instagram : {form.cleaned_data['instagram']}</p>"
        sendMail(subject,text_content,html_content)
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return redirect('organizer:register-complete')

class OrgRegisterComplete(TemplateView):
    template_name = "org-register-complete.html"


class OrganizerProfile(TemplateView):
    template_name = 'organizer-profile.html'


class OrganizerListView(ListView):
    model = Organizer
    context_object_name = 'organizers'
    template_name = "organizer-list.html"
    paginate_by = 12

    def get_queryset(self):
        if self.request.method == 'GET':

            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset1 = Organizer.objects.filter(organizer_name__icontains=title_name)
                return queryset1

        return super().get_queryset().all()


class OrganizerEditView(UpdateView, LoginRequiredMixin):
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
        print('okk')
        form.instance.organizer = self.request.user.organizer
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(self.request)
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
        print(super().get_queryset().filter(organizer=self.request.user.organizer))
        return super().get_queryset().filter(organizer=self.request.user.organizer)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activities"] = Activity.objects.filter(organizer=self.request.user.organizer)
        context['trainings'] = Training.objects.filter(organizer=self.request.user.organizer)
        return context


def OrganizerDetail(request, pk):
    organizer = Organizer.objects.get(pk=pk)
    images = OrganizerImage.objects.filter(organizer=organizer)
    tours = Tour.objects.filter(organizer=organizer, status=1)
    trainings = Training.objects.filter(organizer=organizer, status=1)
    activities = Activity.objects.filter(organizer=organizer, status=1)

    guides = Guide.objects.filter(organizer=organizer)
    instructors = Instructor.objects.filter(organizer=organizer)

    context = {
        'organizer': organizer,
        'images': images,
        'tours': tours,
        'trainings': trainings,
        'activities': activities,
        'guides' : guides,
        'instructors' : instructors
    }
    return render(request, 'company-profile.html', context)


def organizer_image_list(request, pk):
    organizer = Organizer.objects.get(pk=pk)
    image = OrganizerImage.objects.filter(organizer=organizer)

    context = {
        'organizer': organizer,
        'image_list': image,
    }
    return render(request, 'image-list.html', context)



class TourImageUpdateView(UpdateView):
    model = TourImage
    form_class = OrganizerTourImageForm
    template_name = "tour-images-edit.html"


class TourDeleteView(DeleteView):
    model = Tour

    def get_success_url(self):
        return reverse_lazy('organizer:organizer-actions')


class ActivityUpdateView(UpdateView):
    model = Activity
    form_class = OrganizerActivityForm
    template_name = "tour-edit.html"

    def get_success_url(self):
        return reverse_lazy('activity:detail', args = (self.kwargs['pk'],))

class ActivityDeleteView(DeleteView):
    model = Activity

    def get_success_url(self):
        return reverse_lazy('organizer:organizer-actions')

class TrainingUpdateView(UpdateView):
    model = Training
    form_class = OrganizerTrainingForm
    template_name = "tour-edit.html"

    def get_success_url(self):
        return reverse_lazy('training:detail', args = (self.kwargs['pk'],))


class DeleteAccessMixin:

    def dispatch(self, request, *args, **kwargs):
        if Training.objects.filter(pk=self.pk):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class TrainingDeleteView(DeleteView):
    model = Training

    def get_success_url(self):
        return reverse_lazy('organizer:organizer-actions')


def finishTour(request, pk):
    tour = Tour.objects.get(pk=pk)
    tour.status = 3
    tour.save()
    return redirect('tour:detail', pk=pk)


def finishActivity(request, pk):
    activity = Activity.objects.get(pk=pk)
    activity.status = 3
    activity.save()
    return redirect('activity:detail', pk=pk)


def finishTraining(request, pk):
    training = Training.objects.get(pk=pk)
    training.status = 3
    training.save()
    return redirect('training:detail', pk=pk)


def TourUpdate(request, pk):

    tour = Tour.objects.get(id=pk)

    TourImageFormSet = inlineformset_factory(Tour, TourImage, form=OrganizerTourImageForm, fields=('image',), extra=5)
    TourScheduleFormSet = inlineformset_factory(Tour, TourSchedule, form=OrganizerTourScheduleForm, fields=('schedule_image',), extra=5)
    TourUrlFormSet = inlineformset_factory(Tour, TourUrl, form=OrganizerTourURLForm, fields=('url',), extra=5)
    # TourDetailFormSet = inlineformset_factory(Tour, TourDetail, form=OrganizerTourDetailForm, extra=5)


    if request.method == 'POST':

        tour_form = OrganizerTourForm(request.POST or None, request.FILES or None, instance=tour)
        # detail_form = TourDetailFormSet(request.POST or None, instance=tour)
        url_form = TourUrlFormSet(request.POST or None, instance=tour)
        image_form = TourImageFormSet(request.POST or None, request.FILES or None, instance=tour)
        schedule_form = TourScheduleFormSet(request.POST or None, request.FILES or None, instance=tour)
        print(request.POST)

        print(tour_form.is_valid(),url_form.is_valid() , image_form.is_valid() , schedule_form.is_valid())

        if tour_form.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():

            tour_form.save()
            # detail_form.save()
            url_form.save()
            image_form.save()
            schedule_form.save()

            return redirect('tour:detail', pk=pk)


    else:
        context = {
            'tour_form': OrganizerTourForm(instance=tour),
            # 'detail_form': TourDetailFormSet(instance=tour),
            'url_form': TourUrlFormSet(instance=tour),
            'image_form':TourImageFormSet(instance=tour),
            'schedule_form': TourScheduleFormSet(instance=tour),
            'tour_organizer' : tour.organizer
        }
        return render(request, 'tour-edit.html', context)


def ActivityUpdate(request, pk):

    activity = Activity.objects.get(id=pk)

    ActivityImageFormSet = inlineformset_factory(Activity, ActivityImage, form=OrganizerActivityImageForm, fields=('image',), extra=5)
    ActivityScheduleFormSet = inlineformset_factory(Activity, ActivitySchedule, form=OrganizerActivityScheduleForm, fields=('schedule_image',), extra=5)
    ActivityUrlFormSet = inlineformset_factory(Activity, ActivityUrl, form=OrganizerActivityURLForm, fields=('url',), extra=5)

    # ActivityDetailFormSet = inlineformset_factory(Activity, ActivityDetail, form=OrganizerActivityDetailForm, extra=5)

    if request.method == 'POST':

        activity_form = OrganizerActivityForm(request.POST or None, request.FILES or None, instance=activity)
        # detail_form = ActivityDetailFormSet(request.POST or None, instance=activity)
        url_form = ActivityUrlFormSet(request.POST or None, instance=activity)

        image_form = ActivityImageFormSet(request.POST or None, request.FILES or None, instance=activity)
        schedule_form = ActivityScheduleFormSet(request.POST or None, request.FILES or None, instance=activity)

        if activity_form.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():

            activity_form.save()
            # detail_form.save()
            url_form.save()
            image_form.save()
            schedule_form.save()

            return redirect('activity:detail', pk=pk)


    else:
        context = {
            'tour_form': OrganizerActivityForm(instance=activity),
            # 'detail_form': ActivityDetailFormSet(instance=activity),
            'url_form': ActivityUrlFormSet(instance=activity),
            'image_form':ActivityImageFormSet(instance=activity),
            'schedule_form': ActivityScheduleFormSet(instance=activity),
            'activity_organizer':activity.organizer
        }
        return render(request, 'activity-edit.html', context)


def TrainingUpdate(request, pk):

    training = Training.objects.get(id=pk)

    TrainingImageFormSet = inlineformset_factory(Training, TrainingImage, form=OrganizerTrainingImageForm, fields=('image',), extra=5)
    TrainingScheduleFormSet = inlineformset_factory(Training, TrainingSchedule, form=OrganizerTrainingScheduleForm, fields=('schedule_image',), extra=5)
    TrainingUrlFormSet = inlineformset_factory(Training, TrainingUrl, form=OrganizerTrainingURLForm, fields=('url',), extra=5)

    # TrainingDetailFormSet = inlineformset_factory(Training, TrainingDetail, form=OrganizerTrainingDetailForm, extra=5)

    if request.method == 'POST':

        training_form = OrganizerTrainingForm(request.POST or None, request.FILES or None, instance=training)
        # detail_form = TrainingDetailFormSet(request.POST or None, instance=training)
        url_form = TrainingUrlFormSet(request.POST or None, instance=training)

        image_form = TrainingImageFormSet(request.POST or None, request.FILES or None, instance=training)
        schedule_form = TrainingScheduleFormSet(request.POST or None, request.FILES or None, instance=training)

        if training_form.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():

            training_form.save()
            # detail_form.save()
            url_form.save()
            image_form.save()
            schedule_form.save()

            return redirect('training:detail', pk=pk)


    else:
        context = {
            'tour_form': OrganizerTrainingForm(instance=training),
            # 'detail_form': TrainingDetailFormSet(instance=training),
            'url_form': TrainingUrlFormSet(instance=training),
            'image_form':TrainingImageFormSet(instance=training),
            'schedule_form': TrainingScheduleFormSet(instance=training),
            'training_organizer':training.organizer
        }
        return render(request, 'training-edit.html', context)


def OrganizerTour(request):
    image_formset = modelformset_factory(TourImage, fields=('image', ), extra=10, form=OrganizerTourImageForm, validate_max=2)
    schedule_formset = modelformset_factory(TourSchedule, fields=('schedule_image', ), extra=10, form=OrganizerTourScheduleForm)
    url_formset = modelformset_factory(TourUrl, fields = ('url',), extra=10, form = OrganizerTourURLForm)
    # detail_formset = modelformset_factory(TourDetail, extra=10, form=OrganizerTourDetailForm)

    if request.method == 'POST':
        print(request.POST)
        tour_form = OrganizerTourForm(request.POST or None, request.FILES or None)
        # detail_form = detail_formset(request.POST or None)
        url_form = url_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)
        print(tour_form.is_valid(), url_form.is_valid() , image_form.is_valid() , schedule_form.is_valid())
        # print(tour_form.errors, image_form.errors, schedule_form.errors)
        if tour_form.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            tour = tour_form.save(commit=False)
            tour.organizer = request.user.organizer
            tour.status = 2
            tour.save()

            # start_date = datetime.strptime(request.POST.get('datefrom'), "%Y-%m-%d")
            # end_date = datetime.strptime(request.POST.get('dateto'), "%Y-%m-%d")
            # print((end_date-start_date).days, 'days')

            subject = f'New tour added by {tour.organizer.organizer_name}'
            text_content = f'New tour added by {tour.organizer.organizer_name}'
            html_content = f"<p>Name : {tour.title}</p><p>Location : {tour.address} , {tour.city} {tour.country}</p><p>Owner : {tour.organizer.organizer_name}</p>"
            sendMail(subject,text_content,html_content)

            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.tour = tour
                    image.save()

            # for i in detail_form:
            #     print('az',i.cleaned_data)

            #     if i.cleaned_data:
            #         detail = i.save(commit=False)
            #         detail.tour = tour
            #         detail.save()


            for i in url_form:
                if i.cleaned_data:
                    url = i.save(commit=False)
                    url.tour = tour
                    url.save()

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
            # 'detail_form': detail_formset(queryset=TourDetail.objects.none()),
            'url_form': url_formset(queryset=TourUrl.objects.none()),
            'image_form': image_formset(queryset=TourImage.objects.none()),
            'schedule_form': schedule_formset(queryset=TourSchedule.objects.none())
        }
        return render(request, 'add-tour.html', context)


def OrganizerActivity(request):
    image_formset = modelformset_factory(ActivityImage, fields=('image', ), extra=10, form=OrganizerActivityImageForm)
    # detail_formset = modelformset_factory(ActivityDetail, extra=10, form=OrganizerActivityDetailForm)
    url_formset = modelformset_factory(ActivityUrl, fields = ('url',), extra=10, form = OrganizerActivityURLForm)

    schedule_formset = modelformset_factory(ActivitySchedule, fields=('schedule_image', ), extra=10, form=OrganizerActivityScheduleForm)

    if request.method == 'POST':
        print('ok-1')
        tour_form = OrganizerActivityForm(request.POST or None, request.FILES or None)

        # detail_form = detail_formset(request.POST or None)
        url_form = url_formset(request.POST or None)

        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)

        print(tour_form.is_valid(), url_form.is_valid() , image_form.is_valid() , schedule_form.is_valid())
        if tour_form.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            tour = tour_form.save(commit=False)
            tour.organizer = Organizer.objects.get(user=request.user.id)
            tour.status = 2
            tour.save()

            subject = f'New activity added by {tour.organizer.organizer_name}'
            text_content = f'New activity added by {tour.organizer.organizer_name}'
            html_content = f"<p>Name : {tour.title}</p><p>Location : {tour.address} , {tour.city} {tour.country}</p><p>Owner : {tour.organizer.organizer_name}</p>"
            sendMail(subject,text_content,html_content)

            # for i in detail_form:
            #     if i.cleaned_data:
            #         detail = i.save(commit=False)
            #         detail.activity = tour
            #         detail.save()

            for i in url_form:
                if i.cleaned_data:
                    url = i.save(commit=False)
                    url.activity = tour
                    url.save()

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
            # 'detail_form': detail_formset(queryset=ActivityDetail.objects.none()),
            'url_form' : url_formset(queryset=ActivityUrl.objects.none()),
            'image_form': image_formset(queryset=ActivityImage.objects.none()),
            'schedule_form': schedule_formset(queryset=ActivitySchedule.objects.none())
        }
        return render(request, 'add-activity.html', context)


def OrganizerTraining(request):
    image_formset = modelformset_factory(TrainingImage, fields=('image', ), extra=10, form=OrganizerTrainingImageForm)
    # detail_formset = modelformset_factory(TrainingDetail, extra=10, form=OrganizerTrainingDetailForm)
    url_formset = modelformset_factory(TrainingUrl, fields = ('url',), extra=10, form = OrganizerTrainingURLForm)
    schedule_formset = modelformset_factory(TrainingSchedule, fields=('schedule_image', ), extra=10, form=OrganizerTrainingScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerTrainingForm(request.POST or None, request.FILES or None)
        # detail_form = detail_formset(request.POST or None)
        url_form = url_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)

        print(tour_form.is_valid(), url_form.is_valid() , image_form.is_valid() , schedule_form.is_valid())

        if tour_form.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():

            tour = tour_form.save(commit=False)
            tour.organizer = Organizer.objects.get(user=request.user.id)
            tour.status = 2
            tour.save()

            subject = f'New training added by {tour.organizer.organizer_name}'
            text_content = f'New training added by {tour.organizer.organizer_name}'
            html_content = f"<p>Name : {tour.title}</p><p>Location : {tour.address} , {tour.city} {tour.country}</p><p>Owner : {tour.organizer.organizer_name}</p>"
            sendMail(subject,text_content,html_content)

            # for i in detail_form:
            #     # print(i.cleaned_data, tour)
            #     if i.cleaned_data:
            #         detail = i.save(commit=False)
            #         detail.training = tour
            #         detail.save()


            for i in url_form:
                if i.cleaned_data:
                    url = i.save(commit=False)
                    url.training = tour
                    url.save()

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

            return redirect('training:home')
        else:
            messages.error(request, "Error")
    else:
        context = {
            'tour_form': OrganizerTrainingForm,
            # 'detail_form': detail_formset(queryset=TrainingDetail.objects.none()),
            'url_form' : url_formset(queryset=TrainingUrl.objects.none()),
            'image_form': image_formset(queryset=TrainingImage.objects.none()),
            'schedule_form': schedule_formset(queryset=TrainingSchedule.objects.none())
        }
        return render(request, 'add-training.html', context)



class AllNotifications(LoginRequiredMixin,ListView):
    model = Notification
    context_object_name = 'notifications'
    template_name='notifications.html'

    def dispatch(self, *args, **kwargs):
        return super(AllNotifications, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(user = self.request.user).order_by('-created_at')
        return queryset



def resetNotifications(request):
    notifications = Notification.objects.filter(user = request.user, is_published=True)
    context = {
        'notifications' : notifications
    }
    for notification in notifications:
        notification.is_published = False
        notification.save()

    return redirect(reverse_lazy('organizer:notifications'))

