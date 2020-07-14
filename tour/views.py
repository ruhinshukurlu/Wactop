from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import *
# pip install psycopg2


style = Type.objects.all()
# data = Tour.objects.all()
# country = []
# for i in data:
#     if i.country not in country:
#         country.append(i.country)




def TourList(request):
    data = Tour.objects.all()
    country = []
    for i in data:
        if i.country not in country:
            country.append(i.country)
    data = Tour.objects.filter(status=1)
    paginator = Paginator(data, 2)
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
        'tour': eachpage,
        'page': page_request,
        'paginator': arr,
        'country': country,
        'style': style,
        'link': request.build_absolute_uri(),
        'model': 'tour'
    }
    return render(request, 'tour-list.html', context)


def TourDetailView(request, pk):
    tour = Tour.objects.get(pk=pk)
    image = TourImage.objects.filter(tour=tour)
    schedule = TourSchedule.objects.filter(tour=tour)
    url = TourUrl.objects.filter(tour=tour)
    lang = request.GET.get('lang')
    if lang:
        if lang == 'az':
            detail = TourDetailAZ.objects.filter(tour=tour)
            description = tour.descriptionaz
        elif lang == 'ru':
            detail = TourDetailRU.objects.filter(tour=tour)
            description = tour.descriptionru
        elif lang == 'en':
            detail = TourDetailEN.objects.filter(tour=tour)
            description = tour.descriptionen
    else:
        detail = TourDetailEN.objects.filter(tour=tour)
        description = tour.descriptionen
        lang = 'en'
    

    context = {
        'tour': tour,
        'detail': detail,
        'image': image,
        'schedule': schedule,
        'url': url,
        'description': description,
        'lang': lang
    }
    tour_view = 'tour_'
    tour_view += str(pk)
    tour_view += '_viewed'
    if not request.COOKIES.get(tour_view):
        response = render(request, 'tour-page.html', context)
        response.set_cookie(tour_view, 'true', max_age=604800)
        tour.viewcount += 1
        tour.save()
        context['tour'] = tour
        return response
    return render(request, 'tour-page.html', context)


def TourFilter(request):
    context2 = {}
    data = Tour.objects.all()
    price_query = request.GET.get('price')
    if price_query:
        if price_query == 'high':
            context2['price2'] = 'high'
            data = Tour.objects.all().order_by('-price')
        elif price_query == 'low':
            context2['price2'] = 'low'
            data = Tour.objects.all().order_by('price')
    duration_query = request.GET.get('duration')
    if duration_query:
        if duration_query == 'long':
            context2['duration2'] = 'long'
            data = Tour.objects.all().order_by('-durationday')
        elif duration_query == 'short':
            context2['duration2'] = 'short'
            data = Tour.objects.all().order_by('durationday')
    country_query = request.GET.get('country')
    if country_query:
        context2['country2'] = country_query
        data = Tour.objects.filter(country__icontains=country_query)
    discount_query = request.GET.get('discount')
    if discount_query:
        context2['discount2'] = '1'
        data = Tour.objects.filter(discount__isnull=False)
    style_query = request.GET.get('style')
    if style_query:
        context2['style2'] = style_query
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
        context2['search2'] = request.GET.get('search')
        data = Tour.objects.filter(keyword__icontains=request.GET.get('search'))

    data = data.filter(status=1)
    paginator = Paginator(data, 2)
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
        'tour': eachpage,
        'page': page_request,
        'paginator': arr,
        'country': country,
        'link': request.build_absolute_uri(),
        'style': style,
        'haslink': haslink
    }
    if context2:
        context.update(context2)
        context.update({'query': 1})
    if len(data) == 0:
        context.update( {'notfound': 'No result found'} )
    return render(request, 'tour-list.html', context)