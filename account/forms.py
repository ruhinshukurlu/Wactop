from django import forms
# from django.contrib.auth.models import User
from account.models import *
from organizer.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import CharField, ModelMultipleChoiceField, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import transaction
from account.models import *



class OrganizerRegisterForm(UserCreationForm):
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
                    'id' : "coverimgInp" ,
                }))
    profile_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
                    'id' : "profileimgInp" ,
                }))
    organizer_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'What is your Organizer name?'
                }), label='Organizer Name')
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'What is your Username?'
                }), label='Username')
    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Password'
                    
                }), label = 'Password')
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Confirm Password'
                    
                }), label = 'Confirm Password')
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Email....'

                }),label='Email')
    description = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Description',
                    'cols': "10",
                    'rows' : "5"

                }),label='Description')
    about = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
                    'class': 'form-input',
                    'placeholder' : 'About you...',
                    'cols': "10",
                    'rows' : "5"

                }), label='About')
    address = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Your Address'
                }),label='Address')
    contact_number1 = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Your Contact Number'

                }),label='Contact Number 1')
    contact_number2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Your Contact Number'

                }),label='Contact Number 2')
    website = forms.URLField(max_length=150, widget=forms.URLInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Your Website'

                }),label='Website')
    facebook = forms.URLField(max_length=150, widget=forms.URLInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Your Facebook'

                }),label='Facebook')
    instagram = forms.URLField(max_length=150, widget=forms.URLInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Your Instagram'

                }),label='Instagram')

    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organizer = True
        user.is_active = False
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        organizer = Organizer.objects.create(user=user)
        organizer.cover = self.cleaned_data['cover_image']
        organizer.profile_photo = self.cleaned_data.get('profile_image')
        organizer.organizer_name=self.cleaned_data['organizer_name']
        organizer.descriptionaz=self.cleaned_data['description']
        organizer.about=self.cleaned_data['about']
        organizer.contact_number_1=self.cleaned_data['contact_number1']
        organizer.contact_number_2=self.cleaned_data['contact_number2']
        organizer.address=self.cleaned_data['address']
        organizer.website=self.cleaned_data['website']
        organizer.facebook=self.cleaned_data['facebook']
        organizer.instagram=self.cleaned_data['instagram']
        organizer.save()
        return user
  


class CustomerRegisterForm(UserCreationForm):
    # full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
    #                 'class': 'form-input',
    #                 'placeholder' : 'Full Name *',
    #             }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Username...',
                }), label='Username')
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Email...'

                }), label='Email')
    password1 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Password *',
                }),label='Password')
    password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
                    'class': 'form-input',
                    'placeholder' : 'Confirm Password *',
                }), label='Confirm Password')
                
    # profile_image = forms.FileField('Profile', max_length=, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.is_active = True
        # user.first_name = self.cleaned_data.get('first_name')
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        # customer.phone_number=self.cleaned_data.get('phone_number')
        # customer.location=self.cleaned_data.get('location')
        customer.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Username',
        'class' : 'form-input',
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'placeholder' : 'Password',
        'class' : 'form-input',
    }))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-input',
        'placeholder' : 'Old password'
    }), required=True)

    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-input',
        'placeholder' : 'New password'
    }), required=True)

    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-input',
        'placeholder' : 'Re-enter new password'
    }), required=True)
    

# class UserEditForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = []


class UserEditForm(forms.ModelForm):
    # profile_img = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ['username','email','profile_img']

        widgets = {
            'username': forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Username',
                }),
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-input',
                'placeholder' : 'Email'
            })
        }