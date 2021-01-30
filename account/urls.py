from django.urls import path, include, re_path
from account.views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views 
from django.views.generic import TemplateView
from django.urls import reverse_lazy


app_name = 'account'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('change_password/',ChangePasswordView.as_view(), name = 'change-password'),
    path("user/<int:pk>/update", CustomerUpdateView.as_view(), name="user-update"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = 'reset-password.html',
        success_url = reverse_lazy('account:password_reset_done')),
        name="password_reset"),

    path('reset_password_done/',auth_views.PasswordResetDoneView.as_view(template_name = 'reset-password-done.html'), 
        name="password_reset_done"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), 
        name="password_reset_complete"),
    path('', HomeView.as_view()),
]