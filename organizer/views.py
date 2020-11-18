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
from django.core.mail import send_mail, EmailMultiAlternatives
from Wactop.mail import *
from account.forms import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# from organizer.decorators import user_is_organizer_author



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
       
        return redirect('main:home')


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
    tours = Tour.objects.filter(organizer=organizer)
    trainings = Training.objects.filter(organizer=organizer)
    activities = Activity.objects.filter(organizer=organizer)

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


class TourUpdateView(UpdateView):
    model = Tour
    form_class = OrganizerTourForm
    template_name = "tour-edit.html"

    def get_success_url(self):
        return reverse_lazy('tour:detail', args = (self.kwargs['pk'],))


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

class TrainingDeleteView(DeleteView):
    model = Training

    def get_success_url(self):
        return reverse_lazy('organizer:organizer-actions')

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


def OrganizerTour(request):
    image_formset = modelformset_factory(TourImage, fields=('image', ), extra=10, form=OrganizerTourImageForm, validate_max=2)
    schedule_formset = modelformset_factory(TourSchedule, fields=('image', ), extra=10, form=OrganizerTourScheduleForm)
    url_formset = modelformset_factory(TourUrl, fields = ('url',), extra=10, form = OrganizerTourURLForm)
    detail_formset_en = modelformset_factory(TourDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerTourDetailForm)
    detail_formset_az = modelformset_factory(TourDetailAZ, fields=('title', 'text', ), extra=10, form=OrganizerTourDetailForm)
    detail_formset_ru = modelformset_factory(TourDetailRU, fields=('title', 'text', ), extra=10, form=OrganizerTourDetailForm)

    if request.method == 'POST':
        tour_form = OrganizerTourForm(request.POST or None, request.FILES or None)
        detail_form_en = detail_formset_en(request.POST or None)
        detail_form_az = detail_formset_az(request.POST or None)
        detail_form_ru = detail_formset_ru(request.POST or None)
        url_form = url_formset(request.POST or None)
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)

        # print(tour_form.errors, image_form.errors, schedule_form.errors)
        if tour_form.is_valid() and detail_form_en.is_valid() and detail_form_az.is_valid() and detail_form_ru.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            
            tour = tour_form.save(commit=False)
            tour.organizer = request.user.organizer
            tour.status = 2
            tour.save()
            
            subject = f'New tour added by {tour.organizer.organizer_name}'
            text_content = f'New tour added by {tour.organizer.organizer_name}'
            html_content = f"<p>Name : {tour.title}</p><p>Location : {tour.address} , {tour.city} {tour.country}</p><p>Owner : {tour.organizer.organizer_name}</p>"
            sendMail(subject,text_content,html_content)

            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.tour = tour
                    image.save()

            for i in detail_form_en:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()

            for i in detail_form_az:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()

            for i in detail_form_ru:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()
            
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
            'detail_form_en': detail_formset_en(queryset=TourDetailEN.objects.none()),
            'detail_form_az': detail_formset_az(queryset=TourDetailAZ.objects.none()),
            'detail_form_ru': detail_formset_ru(queryset=TourDetailRU.objects.none()),
            'url_form': url_formset(queryset=TourUrl.objects.none()),
            'image_form': image_formset(queryset=TourImage.objects.none()),
            'schedule_form': schedule_formset(queryset=TourSchedule.objects.none())
        }
        # return render(request, 'organizer-post.html', context)
        return render(request, 'add-tour.html', context)


def OrganizerActivity(request):
    image_formset = modelformset_factory(ActivityImage, fields=('image', ), extra=10, form=OrganizerActivityImageForm)
    detail_formset_en = modelformset_factory(ActivityDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerActivityDetailForm)
    detail_formset_az = modelformset_factory(ActivityDetailAZ, fields=('title', 'text', ), extra=10, form=OrganizerActivityDetailForm)
    detail_formset_ru = modelformset_factory(ActivityDetailRU, fields=('title', 'text', ), extra=10, form=OrganizerActivityDetailForm)
    url_formset = modelformset_factory(ActivityUrl, fields = ('url',), extra=10, form = OrganizerActivityURLForm)

    schedule_formset = modelformset_factory(ActivitySchedule, fields=('image', ), extra=10, form=OrganizerActivityScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerActivityForm(request.POST or None, request.FILES or None)

        detail_form_en = detail_formset_en(request.POST or None)
        detail_form_az = detail_formset_az(request.POST or None)
        detail_form_ru = detail_formset_ru(request.POST or None)
        url_form = url_formset(request.POST or None)
        
        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)

        if tour_form.is_valid() and detail_form_en.is_valid() and detail_form_az.is_valid() and detail_form_ru.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
            tour = tour_form.save(commit=False)
            tour.organizer = Organizer.objects.get(user=request.user.id)
            tour.status = 2
            tour.save()

            subject = f'New activity added by {tour.organizer.organizer_name}'
            text_content = f'New activity added by {tour.organizer.organizer_name}'
            html_content = f"<p>Name : {tour.title}</p><p>Location : {tour.address} , {tour.city} {tour.country}</p><p>Owner : {tour.organizer.organizer_name}</p>"
            sendMail(subject,text_content,html_content)
            for i in detail_form_en:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()

            for i in detail_form_az:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()

            for i in detail_form_ru:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()
            
            for i in url_form:
                if i.cleaned_data:
                    url = i.save(commit=False)
                    url.tour = tour
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
            'detail_form_en': detail_formset_en(queryset=ActivityDetailEN.objects.none()),
            'detail_form_az': detail_formset_az(queryset=ActivityDetailAZ.objects.none()),
            'detail_form_ru': detail_formset_ru(queryset=ActivityDetailRU.objects.none()),
            'url_form' : url_formset(queryset=ActivityUrl.objects.none()),
            'image_form': image_formset(queryset=ActivityImage.objects.none()),
            'schedule_form': schedule_formset(queryset=ActivitySchedule.objects.none())
        }
        return render(request, 'add-activity.html', context)


def OrganizerTraining(request):
    image_formset = modelformset_factory(TrainingImage, fields=('image', ), extra=10, form=OrganizerTrainingImageForm)
    detail_formset_en = modelformset_factory(TrainingDetailEN, fields=('title', 'text', ), extra=10, form=OrganizerTrainingDetailForm)
    detail_formset_az = modelformset_factory(TrainingDetailAZ, fields=('title', 'text', ), extra=10, form=OrganizerTrainingDetailForm)
    detail_formset_ru = modelformset_factory(TrainingDetailRU, fields=('title', 'text', ), extra=10, form=OrganizerTrainingDetailForm)
    url_formset = modelformset_factory(TrainingUrl, fields = ('url',), extra=10, form = OrganizerTrainingURLForm)
    schedule_formset = modelformset_factory(TrainingSchedule, fields=('image', ), extra=10, form=OrganizerTrainingScheduleForm)

    if request.method == 'POST':
        tour_form = OrganizerTrainingForm(request.POST or None, request.FILES or None)

        detail_form_en = detail_formset_en(request.POST or None)
        detail_form_az = detail_formset_az(request.POST or None)
        detail_form_ru = detail_formset_ru(request.POST or None)
        url_form = url_formset(request.POST or None)

        image_form = image_formset(request.POST or None, request.FILES or None)
        schedule_form = schedule_formset(request.POST or None, request.FILES or None)
        if tour_form.is_valid() and detail_form_en.is_valid() and detail_form_az.is_valid() and detail_form_ru.is_valid() and url_form.is_valid() and image_form.is_valid() and schedule_form.is_valid():
           
            tour = tour_form.save(commit=False)
            tour.organizer = request.user.organizer

            tour.status = 2
            tour.save()

            subject = f'New training added by {tour.organizer.organizer_name}'
            text_content = f'New training added by {tour.organizer.organizer_name}'
            html_content = f"<p>Name : {tour.title}</p><p>Location : {tour.address} , {tour.city} {tour.country}</p><p>Owner : {tour.organizer.organizer_name}</p>"
            sendMail(subject,text_content,html_content)

            for i in detail_form_en:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()

            for i in detail_form_az:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()

            for i in detail_form_ru:
                if i.cleaned_data:
                    detail = i.save(commit=False)
                    detail.tour = tour
                    detail.save()
            
            for i in url_form:
                if i.cleaned_data:
                    url = i.save(commit=False)
                    url.tour = tour
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
            'detail_form_en': detail_formset_en(queryset=TrainingDetailEN.objects.none()),
            'detail_form_az': detail_formset_az(queryset=TrainingDetailAZ.objects.none()),
            'detail_form_ru': detail_formset_ru(queryset=TrainingDetailRU.objects.none()),
            'url_form' : url_formset(queryset=TrainingUrl.objects.none()),
            'image_form': image_formset(queryset=TrainingImage.objects.none()),
            'schedule_form': schedule_formset(queryset=TrainingSchedule.objects.none())
        }
        return render(request, 'add-training.html', context)


