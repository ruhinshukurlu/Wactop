from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import CharField, ModelMultipleChoiceField, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import transaction
from .models import *
from tour.models import *
from activity.models import *
from training.models import *



class OrganizerPhotoForm(forms.ModelForm):
    class Meta:
        model = OrganizerImage
        fields = ('image', )


class GuideForm(forms.ModelForm):

    class Meta:
        model = Guide
        fields = ['name','surname','experience','certification']

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-input',
            }),
            'surname' : forms.TextInput(attrs={
                'class' : 'form-input',
            }),
            'experience' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'certification' : forms.TextInput(attrs={
                'class' : 'form-input',
            })
        }


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = ['name','surname','experience','certification']

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-input',
            }),
            'surname' : forms.TextInput(attrs={
                'class' : 'form-input',
            }),
            'experience' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'certification' : forms.TextInput(attrs={
                'class' : 'form-input',
            })
        }


class OrganizerPhotoEditForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo')

    class Meta:
        model = TrainingImage
        fields = ('image', )


class OrganizerTourForm(forms.ModelForm):
    title = forms.CharField(label='Tour Title', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Enter Title'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Country...'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'City...'}))

    datefrom = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }))
    dateto = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }))

    guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    descriptionen = forms.CharField(label = 'Tour Description in Engilsh', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about tour...', 'rows' : '5'}))
    descriptionaz = forms.CharField(label = 'Tour Description in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about tour...', 'rows' : '5'}))
    descriptionru = forms.CharField(label = 'Tour Description in Russia', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about tour...', 'rows' : '5'}))
    
    class Meta:
        model = Tour
        fields = [ 'title','city','country','address','guide','descriptionen', 'descriptionaz', 'descriptionru', 'tour_type', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', ]

        widgets = {

            'avatar' : forms.ClearableFileInput(attrs = {
                'id' : 'profilePhotoExample'
            }),
            'cover' : forms.ClearableFileInput(attrs = {
                'id' : 'coverPhotoInput'
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Price...'
            }),
            'pricefor' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Price for...'
            }),
            'currency' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'tour_type' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'durationday' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Duration Day...'
            }),
            'durationnight' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Duration Night...'
            }),
            'address' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Address'
            })
        }



class OrganizerTourDetailForm(forms.ModelForm):

    title = forms.CharField(label='Tour Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TourDetailEN
        fields = ('title', 'text', )



class OrganizerTourImageForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo', widget = forms.ClearableFileInput(attrs={
        'class' : 'photo-input'
    }))

    class Meta:
        model = TourImage
        fields = ('image', )

class OrganizerTourScheduleForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Schedule', widget = forms.ClearableFileInput(attrs={
        'class' : 'schedule-input'
    }))

    class Meta:
        model = TourSchedule
        fields = ('image', )

class OrganizerTourURLForm(forms.ModelForm):

    class Meta:
        model = TourUrl
        fields = ('url',)

        widgets = {
            'url' : forms.URLInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Add URL here'
            })
        }


class OrganizerActivityForm(forms.ModelForm):
    title = forms.CharField(label='Activity Title', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Enter Title'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Country...'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'City...'}))

    datefrom = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }))
    dateto = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }))

    guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    descriptionen = forms.CharField(label = 'Activity Description in English', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about activity...', 'rows' : '5'}))
    descriptionaz = forms.CharField(label = 'Activity Description in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about activity...', 'rows' : '5'}))
    descriptionru = forms.CharField(label = 'Activity Description in Russia', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about activity...', 'rows' : '5'}))
    
    class Meta:
        model = Activity
        fields = [ 'title','city','country','address','guide','descriptionen','descriptionaz','descriptionru', 'activity_type', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', ]

        widgets = {

            'avatar' : forms.ClearableFileInput(attrs = {
                'id' : 'profilePhotoExample'
            }),
            'cover' : forms.ClearableFileInput(attrs = {
                'id' : 'coverPhotoInput'
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Price...'
            }),
            'pricefor' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Price for...'
            }),
            'currency' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'activity_type' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'durationday' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Duration Day...'
            }),
            'durationnight' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Duration Night...'
            }),
            'address' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Address'
            })
        }
    

class OrganizerActivityDetailForm(forms.ModelForm):

    title = forms.CharField(label='Activity Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))

    class Meta:
        model = ActivityDetailEN
        fields = ('title', 'text', )

class OrganizerActivityURLForm(forms.ModelForm):

    class Meta:
        model = ActivityUrl
        fields = ('url',)

        widgets = {
            'url' : forms.URLInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Add URL here'
            })
        }


class OrganizerActivityImageForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo', widget = forms.ClearableFileInput(attrs={
        'class' : 'photo-input'
    }))

    class Meta:
        model = ActivityImage
        fields = ('image', )

class OrganizerActivityScheduleForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Schedule', widget = forms.ClearableFileInput(attrs={
        'class' : 'schedule-input'
    }))

    class Meta:
        model = ActivitySchedule
        fields = ('image', )


class OrganizerTrainingForm(forms.ModelForm):
    title = forms.CharField(label='Tour Title', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Enter Title'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Country...'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'City...'}))

    datefrom = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }))
    dateto = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }))

    guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    descriptionen = forms.CharField(label = 'Training Description in English', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    descriptionaz = forms.CharField(label = 'Training Description in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    descriptionru = forms.CharField(label = 'Training Description in Russia', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    
    class Meta:
        model = Training
        fields = ['title', 'descriptionen','descriptionaz','descriptionru', 'training_type', 'country', 'city','address', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', ]

        widgets = {

            'avatar' : forms.ClearableFileInput(attrs = {
                'id' : 'profilePhotoExample'
            }),
            'cover' : forms.ClearableFileInput(attrs = {
                'id' : 'coverPhotoInput'
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Price...'
            }),
            'pricefor' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Price for...'
            }),
            'currency' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'training_type' : forms.Select(attrs={
                'class' : 'custom-select',
            }),
            'durationday' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Duration Day...'
            }),
            'durationnight' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Duration Night...'
            }),
            'address' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Address'
            })
        }


class OrganizerTrainingDetailForm(forms.ModelForm):
    title = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TrainingDetailEN
        fields = ('title', 'text', )

class OrganizerTrainingURLForm(forms.ModelForm):

    class Meta:
        model = TrainingUrl
        fields = ('url',)

        widgets = {
            'url' : forms.URLInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Add URL here'
            })
        }


class OrganizerTrainingImageForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo', widget = forms.ClearableFileInput(attrs={
        'class' : 'photo-input'
    }))

    class Meta:
        model = TrainingImage
        fields = ('image', )


class OrganizerTrainingScheduleForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Schedule', widget = forms.ClearableFileInput(attrs={
        'class' : 'schedule-input'
    }))

    class Meta:
        model = TrainingSchedule
        fields = ('image', )


class OrganizerEditForm(forms.ModelForm):

    descriptionen = forms.CharField(label = 'Description', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about organizer...', 'rows' : '5'}))
    # descriptionaz = forms.CharField(label = 'Description in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about organizer...', 'rows' : '5'}))
    # descriptionru = forms.CharField(label = 'Description in Russia', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about organizer...', 'rows' : '5'}))
    
    class Meta:
        model = Organizer
        fields = ['organizer_name', 'email', 'descriptionen', 'organizer_type', 'about', 'website', 'facebook', 'instagram', 'address', 'contact_number_1', 'contact_number_2', 'profile_photo', 'cover']

        widgets = {
            'organizer_type' : forms.Select(attrs={
                'class' : 'custom-select'
            }),
            'descriptionen' : forms.Textarea(attrs={
                'rows' : '5'
            }),
            'about' : forms.Textarea(attrs={
                'rows' : '5'
            }),
            'cover' : forms.ClearableFileInput(attrs={
                'id' : 'coverPhoto'
            }),
            'profile_photo' : forms.ClearableFileInput(attrs={
                'id' : 'profilePhoto'
            })
        }



