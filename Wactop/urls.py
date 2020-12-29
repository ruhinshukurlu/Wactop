from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from django.urls import reverse_lazy
import notifications.urls

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('', include('main.urls', namespace='main')),
    path('account/', include('account.urls', namespace='account')),
    path('organizer/', include('organizer.urls', namespace='organizer')),
    path('tour/', include('tour.urls', namespace='tour')),
    path('training/', include('training.urls', namespace='training')),
    path('activity/', include('activity.urls', namespace='activity')),
    path('api/', include('api.urls', namespace='api')),
    path('social-auth/', include('social_django.urls', namespace="social")), 
    path('password_reset_confirm//<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html',success_url = reverse_lazy('account:password_reset_complete')), 
        name="password_reset_confirm"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)