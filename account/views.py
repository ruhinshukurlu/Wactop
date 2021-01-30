from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import get_user_model, login

from account.forms import *
# from account.models import *
from account.tokens import account_activation_token
# Create your views here.

User = get_user_model()

class UserRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'register-user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('email/account_activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return render( self.request , 'email/success_email.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render( request , 'email/confirmation_done.html')
    else:
        return render( request , 'email/invalid.html')


class ChangePasswordView(PasswordChangeView):
    template_name = 'change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('main:home')



class CustomerUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user-edit.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('main:home')


class HomeView(TemplateView):
    template_name = "test.html"