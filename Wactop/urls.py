from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('account/', include('account.urls', namespace='account')),
    path('organizer/', include('organizer.urls', namespace='organizer')),
    path('tour/', include('tour.urls', namespace='tour')),
    path('training/', include('training.urls', namespace='training')),
    path('activity/', include('activity.urls', namespace='activity')),
    path('api/', include('api.urls', namespace='api')),
    path('social-auth/', include('social_django.urls', namespace="social")), 

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)