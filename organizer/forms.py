from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import CharField, ModelMultipleChoiceField, ModelChoiceField
from tour.models import *
from activity.models import *
from training.models import *


class UserRegisterForm(UserCreationForm):   
    # username = UsernameField(
    #     widget = forms.TextInput(
    #         attrs={
    #             'placeholder' : 'Username',
    #             'id': 'username'
    #             # 'class' : 'form-control',
    #         }))
    # password1 = forms.CharField(
    #     widget = forms.PasswordInput(
    #         attrs={
    #             'placeholder' : 'Password',
    #         }))
    # password2 = forms.CharField(
    #     widget = forms.PasswordInput(
    #         attrs={
    #             'placeholder' : 'Confirm password',
    #          }))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class OrganizerRegisterForm(forms.ModelForm):
    # email = forms.EmailField(
    #     widget = forms.EmailInput(
    #         attrs={
    #             'placeholder' : 'Email',
    #         }))
    # avatar = forms.ImageField(
    #     widget = forms.FileInput(
    #         attrs={
    #             'class': 'input-file'
    #         }
    #     )
    # )
    class Meta:
        model = Organizer
        fields = ['name', 'email', 'descriptionen', 'type', 'about', 'website', 'facebook', 'instagram', 'adress', 'number1', 'number2', 'avatar', 'cover']


class LoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-txt'}))
    # password = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-psw'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'email', 'type', 'about', 'adress', 'number1', 'number2', 'avatar']

class OrganizerImageRegisterForm(forms.ModelForm):
    class Meta:
        model = OrganizerImage
        fields = ('image', )


class OrganizerTourForm(forms.ModelForm):
    # type = ModelMultipleChoiceField(queryset=Type.objects.all(),required=False)
    datefrom = forms.DateField(widget = forms.SelectDateWidget())
    dateto = forms.DateField(widget = forms.SelectDateWidget())
    class Meta:
        model = Tour
        fields = ['title', 'descriptionen', 'type', 'country', 'city', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', 'guide', ]

class OrganizerTourDetailForm(forms.ModelForm):
    class Meta:
        model = TourDetailEN
        fields = ('title', 'text', )

class OrganizerTourImageForm(forms.ModelForm):
    class Meta:
        model = TourImage
        fields = ('image', )

class OrganizerTourScheduleForm(forms.ModelForm):
    class Meta:
        model = TourSchedule
        fields = ('image', )


class OrganizerActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'descriptionen', 'type', 'country', 'city', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', ]

class OrganizerActivityDetailForm(forms.ModelForm):
    class Meta:
        model = ActivityDetailEN
        fields = ('title', 'text', )

class OrganizerActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = ('image', )

class OrganizerActivityScheduleForm(forms.ModelForm):
    class Meta:
        model = ActivitySchedule
        fields = ('image', )


class OrganizerTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['title', 'descriptionen', 'type', 'country', 'city', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', ]

class OrganizerTrainingDetailForm(forms.ModelForm):
    class Meta:
        model = TrainingDetailEN
        fields = ('title', 'text', )

class OrganizerTrainingImageForm(forms.ModelForm):
    class Meta:
        model = TrainingImage
        fields = ('image', )

class OrganizerTrainingScheduleForm(forms.ModelForm):
    class Meta:
        model = TrainingSchedule
        fields = ('image', )

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Organizer
#         fields = ['name', 'email', 'descriptionen', 'type', 'about', 'website', 'facebook', 'instagram', 'adress', 'number1', 'number2', 'avatar', 'cover']
