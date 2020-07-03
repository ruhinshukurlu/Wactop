from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import *
from tour.models import *   
# pip install psycopg2


style = Type.objects.all()
data = Training.objects.all()
country = []
for i in data:
    if i.country not in country:
        country.append(i.country)




def TrainingList(request):
    data = Training.objects.all()
    country = []
    for i in data:
        if i.country not in country:
            country.append(i.country)
    data = Training.objects.filter(status=1)
    paginator = Paginator(data, 1)
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
    

    context = {
        'tour': training,
        'detail': detail,
        'image': image,
        'schedule': schedule,
        'url': url,
        'description': description,
        'lang': lang
    }
    training_view = 'training_'
    training_view += str(pk)
    training_view += '_viewed'
    if not request.COOKIES.get(training_view):
        response = render(request, 'tour-page.html', context)
        response.set_cookie(training_view, 'true', max_age=604800)
        training.viewcount += 1
        training.save()
        context['tour'] = training
        return response
    return render(request, 'tour-page.html', context)


def TrainingFilter(request):
    context2 = {}
    data = Training.objects.all()
    price_query = request.GET.get('price')
    if price_query:
        if price_query == 'high':
            data = Training.objects.all().order_by('-price')
            context2['price'] = 'high'
        elif price_query == 'low':
            data = Training.objects.all().order_by('price')
            context2['price'] = 'low'
    duration_query = request.GET.get('duration')
    if duration_query:
        if duration_query == 'long':
            data = Training.objects.all().order_by('-durationday')
        elif duration_query == 'short':
            data = Training.objects.all().order_by('durationday')
    country_query = request.GET.get('country')
    if country_query:
        data = Training.objects.filter(country__icontains=country_query)
    discount_query = request.GET.get('discount')
    if discount_query:
        data = Training.objects.filter(discount__isnull=False)
    style_query = request.GET.get('style')
    if style_query:
        notnull = False
        for i in type_choices:
            if i[1] == style_query:
                x = i[0]
        idArr =[]
        for i in data:
            for j in i.type:
                n = int(j)
                if x == n:
                    idArr.append(i.pk)
                    notnull = True
        for i in data:
            if i.pk not in idArr:
                data = data.exclude(pk=i.pk)
    
    if request.GET.get('search'):
        data = Training.objects.filter(keyword__icontains=request.GET.get('search'))
    data = data.filter(status=1)
    paginator = Paginator(data, 1)
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
    haslink = True

    context = {
        'training': eachpage,
        'page': page_request,
        'paginator': arr,
        'country': country,
        'link': request.build_absolute_uri(),
        'style': style,
        'haslink': haslink
    }
    if len(data) == 0:
        context.update( {'notfound' : 'No result found'} )
    return render(request, 'training-list.html', context)