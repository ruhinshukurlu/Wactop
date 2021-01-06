from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from training.forms import CommentForm
from .models import *
from tour.models import *   
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Avg


training_types = TourType.objects.all()
training_type_list = []
if training_types:
    for training_type in training_types:
        if training_type.title not in training_type_list:
            training_type_list.append(training_type.title)

trainings = Training.objects.all()
training_country_list = []
if trainings:
    for training in trainings:
        if training.country not in training_country_list:
            training_country_list.append(training.country)



class TrainingListView(ListView):
    model = Training
    context_object_name = 'trainings'
    template_name = "training-list.html"
    paginate_by = 16

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset1 = Training.objects.filter(status=1)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset1 = queryset1.filter(title__icontains=title_name)
                return queryset1
        return super().get_queryset().filter(status=1)

    def get_context_data(self, **kwargs):
        context = super(TrainingListView, self).get_context_data(**kwargs)

        context['countries'] = training_country_list
        context['training_types'] = training_type_list
        return context


def TrainingList(request):

    data = Training.objects.all()
    country = []
    for i in data:
        if i.country not in country:
            country.append(i.country)
    data = Training.objects.filter(status=1)
    paginator = Paginator(data, 30)
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
        'training': eachpage,
        'page': page_request,
        'paginator': arr,
        'country': country,
        'style': style,
        'link': request.build_absolute_uri()
    }
    return render(request, 'training-list.html', context)


def TrainingDetailView(request, pk):
    training = Training.objects.get(pk=pk)
    image = TrainingImage.objects.filter(training=training)
    schedule = TrainingSchedule.objects.filter(training=training)
    url = TrainingUrl.objects.filter(training=training)
    lang = request.GET.get('lang')
    if lang:
        if lang == 'az':
            detail = TrainingDetailAZ.objects.filter(training=training)
            description = training.descriptionaz
        elif lang == 'ru':
            detail = TrainingDetailRU.objects.filter(training=training)
            description = training.descriptionru
        elif lang == 'en':
            detail = TrainingDetailEN.objects.filter(training=training)
            description = training.descriptionen
    else:
        detail = TrainingDetailEN.objects.filter(training=training)
        description = training.descriptionen
        lang = 'en'

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.POST.get('form_id') == 'myform': 
            textarea = request.POST.get('textarea')
            rating = request.POST.get('rating')
            comment = Comment.objects.create(
                message = textarea,
                rating = rating if rating else 0,
                training = Training.objects.get(pk=pk),
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
            print('salamsalsma', textarea) 
            parent_obj = None
            print('salam')
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                comment = Comment.objects.create(
                    message = textarea,
                    rating = rating,
                    training = Training.objects.get(pk=pk),
                    user = request.user,
                    comment_reply = parent_obj

                )
            else:
                comment = Comment.objects.create(
                    message = textarea,
                    rating = rating,
                    training = Training.objects.get(pk=pk),
                    user = request.user,
                )
             
            response_data = {
                   
            }
            response_data['comments'] = Comment.objects.filter(training = training)
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

    top_tainings = Training.objects.filter(status=1).order_by('rating')[:5]

    context = {
        'top_tainings':top_tainings,
        'tour': training,
        'detail': detail,
        'image': image,
        'schedule': schedule,
        'url': url,
        'description': description,
        'lang': lang,
        'form' : form,
        'comments' : training.comment.filter(comment_reply__isnull=True),
        'comments_count': training.comment.all()

    }
    tour_view = 'tour_'
    tour_view += str(pk)
    tour_view += '_viewed'

    if training.comment.all():
        total_training_comment = int(training.comment.aggregate(Avg('rating')).get('rating__avg', 0))
        print(total_training_comment)
        training.rating = total_training_comment
        training.save()

    if not request.COOKIES.get(tour_view):
        response = render(request, 'training-page.html', context)
        response.set_cookie(tour_view, 'true', max_age=604800)
        training.viewcount += 1
        training.save()
        context['tour'] = training
        return response
    return render(request, 'training-page.html', context)


def update_items(request, pk):
    training = Training.objects.get(pk=pk)

    if request.method == 'POST':
        form = Comment(request.POST)
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
                parent_obj = Comment.objects.get(id=parent_id)
                
                comment = Comment.objects.create(
                    message = textarea,
                    rating = rating,
                    training = Training.objects.get(pk=pk),
                    user = request.user,
                    comment_reply = parent_obj

                )
            else:
                comment = Comment.objects.create(
                    message = textarea,
                    rating = rating,
                    training = Training.objects.get(pk=pk),
                    user = request.user,
                )
             
            response_data = {
                   
            }
            response_data['comments'] = Comment.objects.filter(training = training)
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
        'tour' : training,
        'comments' : training.comment.filter(comment_reply__isnull=True),
        'comments_count': training.comment.all()

    }
    return render(request, 'partials/training-comments.html', context)


def TrainingFilter(request):
    context2 = {}
    data = Training.objects.all()
    price_query = request.GET.get('price')
    if price_query:
        if price_query == 'high':
            data = Training.objects.filter(status=1).order_by('-price')
            context2['price'] = 'high'
        elif price_query == 'low':
            data = Training.objects.filter(status=1).order_by('price')
            context2['price'] = 'low'
    rating_query = request.GET.get('rating')
    if rating_query:
        if rating_query == 'high':
            context2['rating2'] = 'high'
            data = Training.objects.filter(status=1).order_by('-rating')
        elif rating_query == 'low':
            context2['rating2'] = 'low'
            data = Training.objects.filter(status=1).order_by('rating')
    duration_query = request.GET.get('duration')
    if duration_query:
        if duration_query == 'long':
            data = Training.objects.filter(status=1).order_by('-durationday')
        elif duration_query == 'short':
            data = Training.objects.filter(status=1).order_by('durationday')
    country_query = request.GET.get('country')
    if country_query:
        data = Training.objects.filter(country__icontains=country_query, status=1)
        
    discount_query = request.GET.get('discount')
    if discount_query:
        data = Training.objects.filter(discount__isnull=False)

    style_query = request.GET.get('style')
    if style_query:
        context2['style2'] = style_query
        data = Training.objects.filter(training_type=TourType.objects.filter(title=style_query).first().id, status=1)
        

    
    # if request.GET.get('search'):
    #     data = Training.objects.filter(keyword__icontains=request.GET.get('search'))
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
        'trainings': data,
        # 'page': page_request,
        # 'paginator': arr,
        'training_types' : training_type_list,
        'countries': training_country_list,
        # 'link': request.build_absolute_uri(),
        # 'style': style,
        # 'haslink': haslink
    }
    if len(data) == 0:
        context.update( {'notfound' : 'No result found'} )
    return render(request, 'training-list.html', context)