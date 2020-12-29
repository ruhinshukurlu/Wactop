from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView, PasswordResetConfirmView
from account.forms import *
from account.models import *
from django.urls import reverse_lazy

# Create your views here.


class UserRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'register-user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('main:home')


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