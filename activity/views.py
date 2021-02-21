import random

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.db.models import Avg

from .models import *
from tour.models import *
from .forms import *

 
from django.http import HttpResponse, JsonResponse
import json



class ActivityListView(ListView):
    model = Activity
    context_object_name = 'activities'
    template_name = "activity-list.html"
    paginate_by = 16

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset1 = Activity.objects.filter(status=1)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset1.filter(title__icontains=title_name, status=1)
                return queryset

            price_query = self.request.GET.get('price')
            if price_query:
                if price_query == 'high':
                    queryset = Activity.objects.filter(status=1).order_by('-price')
                elif price_query == 'low':
                    queryset = Activity.objects.filter(status=1).order_by('price')
                return queryset

            rating_query = self.request.GET.get('rating')
            if rating_query:
                if rating_query == 'high':
                    queryset = Activity.objects.filter(status=1).order_by('rating')
                    print(queryset)
                elif rating_query == 'low':
                    queryset = Activity.objects.filter(status=1).order_by('-rating')
                return queryset

            duration_query = self.request.GET.get('duration')
            if duration_query:
                if duration_query == 'long':
                    # context2['duration2'] = 'long'
                    queryset = Activity.objects.filter(status=1).order_by('-durationday')
                elif duration_query == 'short':
                    queryset = Activity.objects.filter(status=1).order_by('durationday')
                return queryset

            country_query = self.request.GET.get('country')
            if country_query:
                queryset = Activity.objects.filter(country__icontains=country_query, status=1)
                return queryset
            
            style_query = self.request.GET.get('style')
            if style_query:
                queryset = Activity.objects.filter(activity_type=TourType.objects.filter(title=style_query).first().id,status=1)
                return queryset

            discount_query = self.request.GET.get('discount')
            if discount_query:
                queryset = Activity.objects.filter(discount__gte=1, status=1)
                return queryset
        
        return super().get_queryset().filter(status=1)


    def get_context_data(self, **kwargs):

        activities = Activity.objects.all()
        activity_country_list = []

        if activities:
            for activity in activities:
                if activity.country not in activity_country_list:
                    activity_country_list.append(activity.country)
        
        tour_types = TourType.objects.all()
        tour_type_list = []
        if tour_types:
            for tour_type in tour_types:
                if tour_type.title not in tour_type_list:
                    tour_type_list.append(tour_type.title)

        context = super().get_context_data(**kwargs)
        context["countries"] = activity_country_list
        context['activity_types'] = tour_type_list
        return context


def ActivityDetailView(request, pk):
    activity = Activity.objects.get(pk=pk)
    image = ActivityImage.objects.filter(activity=activity)
    schedule = ActivitySchedule.objects.filter(activity=activity)
    url = ActivityUrl.objects.filter(activity=activity)

    description = {
        'detail_az' : ActivityDetailAZ.objects.filter(activity=activity),
        'description_az' : activity.descriptionaz,
        'detail_ru' : ActivityDetailRU.objects.filter(activity=activity),
        'description_ru' : activity.descriptionru,
        'detail_en' : ActivityDetailEN.objects.filter(activity=activity),
        'description_en' : activity.descriptionen
    }

    

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.POST.get('form_id') == 'myform': 
            textarea = request.POST.get('textarea')
            
            rating = request.POST.get('rating')
            
            comment = ActivityComment.objects.create(
                message = textarea,
                rating = rating if rating else 0,
                activity = Activity.objects.get(pk=pk),
                user = request.user
            )
             
            response_data = {
                   
            }

            return HttpResponse(
                    json.dumps(response_data, indent=4, sort_keys=True, default=str),
                    content_type="application/json"
                )
        
        elif request.POST.get('form_id') == 'p-2 reply-form': 
            textarea = request.POST.get('textarea')
            rating = request.POST.get('rating')
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = ActivityComment.objects.get(id=parent_id)
               
                comment = ActivityComment.objects.create(
                    message = textarea,
                    rating = rating,
                    activity = Activity.objects.get(pk=pk),
                    user = request.user,
                    comment_reply = parent_obj

                )
            else:
                comment = ActivityComment.objects.create(
                    message = textarea,
                    rating = rating,
                    activity = Activity.objects.get(pk=pk),
                    user = request.user,
                )
             
            response_data = {
                   
            }
            response_data['comments'] = ActivityComment.objects.filter(activity = activity)
            return HttpResponse(
                    json.dumps(response_data, indent=4, sort_keys=True, default=str),
                    content_type="application/json"
                )

        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )
    else: 
        form = CommentForm()

    top_activities = sorted(Activity.objects.filter(status=1).order_by('rating')[:5], key=lambda x: random.random())

    context = {
        'top_activities':top_activities,
        'tour': activity,
        'image': image,
        'schedule': schedule,
        'url': url,
        'description': description,
        'form' : form,
        'comments' : activity.activity_comment.filter(comment_reply__isnull=True),
        'comments_count': activity.activity_comment.all()

    }
    tour_view = 'tour_'
    tour_view += str(pk)
    tour_view += '_viewed'

    print(activity.activity_comment.aggregate(Avg('rating')).get('rating__avg', 0))
    if activity.activity_comment.all():
        total_activity_comment = int(activity.activity_comment.aggregate(Avg('rating')).get('rating__avg', 0))
        activity.rating = total_activity_comment
        activity.save()

    if not request.COOKIES.get(tour_view):
        response = render(request, 'activity-page.html', context)
        response.set_cookie(tour_view, 'true', max_age=604800)
        activity.viewcount += 1
        activity.save()
        context['tour'] = activity
        return response
    return render(request, 'activity-page.html', context)


def update_items(request, pk):
    activity = Activity.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.POST.get('form_id') == 'p-2 reply-form': 
            textarea = request.POST.get('textarea')
            rating = request.POST.get('rating')
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = ActivityComment.objects.get(id=parent_id)
                
                comment = ActivityComment.objects.create(
                    message = textarea,
                    rating = rating,
                    activity = Activity.objects.get(pk=pk),
                    user = request.user,
                    comment_reply = parent_obj

                )
            else:
                comment = ActivityComment.objects.create(
                    message = textarea,
                    rating = rating,
                    activity = Activity.objects.get(pk=pk),
                    user = request.user,
                )
             
            response_data = {
                   
            }
            response_data['comments'] = ActivityComment.objects.filter(activity = activity)
            return HttpResponse(
                    json.dumps(response_data, indent=4, sort_keys=True, default=str),
                    content_type="application/json"
                )

        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )
    else: 
        form = CommentForm()

    context = {
        'form' : form,
        'tour' : activity,
        'comments' : activity.activity_comment.filter(comment_reply__isnull=True),
        'comments_count': activity.activity_comment.all()

    }
    return render(request, 'partials/activity-comments.html', context)


def ActivityFilter(request):
    context2 = {}
    data = Activity.objects.all()
    price_query = request.GET.get('price')

    if price_query:
        if price_query == 'high':
            context2['price2'] = 'high'
            data = Activity.objects.filter(status=1).order_by('-price')
        elif price_query == 'low':
            context2['price2'] = 'low'
            data = Activity.objects.filter(status=1).order_by('price')
    rating_query = request.GET.get('rating')
    if rating_query:
        if rating_query == 'high':
            context2['rating2'] = 'high'
            data = Activity.objects.filter(status=1).order_by('-rating')
        elif rating_query == 'low':
            context2['rating2'] = 'low'
            data = Activity.objects.filter(status=1).order_by('rating')

    duration_query = request.GET.get('duration')
    if duration_query:
        if duration_query == 'long':
            context2['duration2'] = 'long'
            data = Activity.objects.filter(status=1).order_by('-durationday')
        elif duration_query == 'short':
            context2['duration2'] = 'short'
            data = Activity.objects.filter(status=1).order_by('durationday')

    country_query = request.GET.get('country')
    if country_query:
        context2['country2'] = country_query
        data = Activity.objects.filter(country__icontains=country_query, status=1)
    
    # discount_query = request.GET.get('discount')
    # if discount_query:
    #     context2['discount2'] = '1'
    #     data = Tour.objects.filter(discount__isnull=False)

    style_query = request.GET.get('style')
    if style_query:
        context2['style2'] = style_query
        data = Activity.objects.filter(activity_type=TourType.objects.filter(title=style_query).first().id, status=1)
        

    # data = Activity.objects.all()
    # price_query = request.GET.get('price')
    # if price_query:
    #     if price_query == 'high':
    #         data = Activity.objects.all().order_by('-price')
    #     elif price_query == 'low':
    #         data = Activity.objects.all().order_by('price')
    # duration_query = request.GET.get('duration')
    # if duration_query:
    #     if duration_query == 'long':
    #         data = Activity.objects.all().order_by('-durationday')
    #     elif duration_query == 'short':
    #         data = Activity.objects.all().order_by('durationday')
    # country_query = request.GET.get('country')
    # if country_query:
    #     data = Activity.objects.filter(country__icontains=country_query)
    # discount_query = request.GET.get('discount')
    # if discount_query:
    #     data = Activity.objects.filter(discount__isnull=False)
    # style_query = request.GET.get('style')
    # if style_query:
    #     notnull = False
    #     for i in type_choices:
    #         if i[1] == style_query:
    #             x = i[0]
    #     idArr =[]
    #     for i in data:
    #         for j in i.type:
    #             n = int(j)
    #             if x == n:
    #                 idArr.append(i.pk)
    #                 notnull = True
    #     for i in data:
    #         if i.pk not in idArr:
    #             data = data.exclude(pk=i.pk)
    
    # if request.GET.get('search'):
    #     data = Activity.objects.filter(keyword__icontains=request.GET.get('search'))
    # data = data.filter(status=1)
    # paginator = Paginator(data, 1)
    # page_request = 'page'
    # page = request.GET.get(page_request)
    # try:
    #     eachpage = paginator.page(page)
    # except PageNotAnInteger:
    #     eachpage = paginator.page(1)
    # except EmptyPage:
    #     eachpage = paginator.page(paginator.num_pages)

    # arr = []
    # for i in range(0, eachpage.paginator.num_pages):
    #     arr.append(i+1)
    # haslink = True

    context = {
        'activities': data,
        # 'page': page_request,
        # 'paginator': arr,
        'countries': activity_country_list,
        # 'link': request.build_absolute_uri(),
        'tour_types': tour_type_list,
        # 'haslink': haslink
    }
    print(context)
    if len(data) == 0:
        context.update( {'notfound' : 'No result found'} )
    return render(request, 'activity-list.html', context)


class ActivityDenyView(CreateView):
    model = ActivityDeny
    form_class = ActivityDenyForm
    template_name = 'deny-message.html'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        activity = Activity.objects.filter(pk = self.kwargs['pk']).first()
        context['object'] = activity
        return context
   
    
    # def form_valid(self, form):
    #     activity = Activity.objects.filter(pk = self.kwargs['pk']).first()
    #     send_mail(
    #         'Subject here',
    #         deny_activity.message,
    #         'sara.axmedova98@gmail.com',
    #         [activity.organizer.user.email],
    #         fail_silently=False,
    #     )   

        return redirect('main:home')

