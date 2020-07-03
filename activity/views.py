from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import *
from tour.models import *
# pip install psycopg2


style = Type.objects.all()
data = Activity.objects.all()
country = []
for i in data:
    if i.country not in country:
        country.append(i.country)




def ActivityList(request):
    data = Activity.objects.all()
    country = []
    for i in data:
        if i.country not in country:
            country.append(i.country)
    style = Type.objects.all()
    data = Activity.objects.filter(status=1)
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
        'activity': eachpage,
        'page': page_request,
        'paginator': arr,
        'country': country,
        'style': style,
        'link': request.build_absolute_uri()
    }
    return render(request, 'activity-list.html', context)


def ActivityDetailView(request, pk):
    activity = Activity.objects.get(pk=pk)
    image = ActivityImage.objects.filter(activity=activity)
    schedule = ActivitySchedule.objects.filter(activity=activity)
    url = ActivityUrl.objects.filter(activity=activity)
    lang = request.GET.get('lang')
    if lang:
        if lang == 'az':
            detail = ActivityDetailAZ.objects.filter(activity=activity)
            description = activity.descriptionaz
        elif lang == 'ru':
            detail = ActivityDetailRU.objects.filter(activity=activity)
            description = activity.descriptionru
        elif lang == 'en':
            detail = ActivityDetailEN.objects.filter(activity=activity)
            description = activity.descriptionen
    else:
        detail = ActivityDetailEN.objects.filter(activity=activity)
        description = activity.descriptionen
        lang = 'en'
    

    context = {
        'tour': activity,
        'detail': detail,
        'image': image,
        'schedule': schedule,
        'url': url,
        'description': description,
        'lang': lang
    }
    activity_view = 'activity_'
    activity_view += str(pk)
    activity_view += '_viewed'
    if not request.COOKIES.get(activity_view):
        response = render(request, 'tour-page.html', context)
        response.set_cookie(activity_view, 'true', max_age=604800)
        activity.viewcount += 1
        activity.save()
        context['activity'] = activity
        return response
    return render(request, 'tour-page.html', context)


def ActivityFilter(request):
    data = Activity.objects.all()
    price_query = request.GET.get('price')
    if price_query:
        if price_query == 'high':
            data = Activity.objects.all().order_by('-price')
        elif price_query == 'low':
            data = Activity.objects.all().order_by('price')
    duration_query = request.GET.get('duration')
    if duration_query:
        if duration_query == 'long':
            data = Activity.objects.all().order_by('-durationday')
        elif duration_query == 'short':
            data = Activity.objects.all().order_by('durationday')
    country_query = request.GET.get('country')
    if country_query:
        data = Activity.objects.filter(country__icontains=country_query)
    discount_query = request.GET.get('discount')
    if discount_query:
        data = Activity.objects.filter(discount__isnull=False)
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
        data = Activity.objects.filter(keyword__icontains=request.GET.get('search'))
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
        'activity': eachpage,
        'page': page_request,
        'paginator': arr,
        'country': country,
        'link': request.build_absolute_uri(),
        'style': style,
        'haslink': haslink
    }
    print(context)
    if len(data) == 0:
        context.update( {'notfound' : 'No result found'} )
    return render(request, 'activity-list.html', context)