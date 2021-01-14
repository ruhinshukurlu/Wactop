from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import CharField, ModelMultipleChoiceField, ModelChoiceField, inlineformset_factory
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

class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = [ 'title','city','country','address','guide','descriptionen', 'descriptionaz', 'descriptionru', 'tour_type', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', 'map_link']

TourInlineFormSet = inlineformset_factory(Tour, TourDetailEN, extra=1, fields = ('title_en', 'text_en'), can_delete=True)


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
        fields = [ 'title','city','country','address','guide','descriptionen', 'descriptionaz', 'descriptionru', 'tour_type', 'price', 'pricefor','discount', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', 'map_link']

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
            }),
            'discount' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Discount'
            }),
            'map_link' : forms.URLInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Add Map link here',
            })
        }



class OrganizerTourDetailEnForm(forms.ModelForm):

    title_en = forms.CharField(label='Tour Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_en = forms.CharField(label='Text in English', widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TourDetailEN
        fields = ('title_en', 'text_en', )

class OrganizerTourDetailAzForm(forms.ModelForm):

    title_az = forms.CharField(label='Tour Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_az = forms.CharField(label='Text in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TourDetailAZ
        fields = ('title_az', 'text_az', )


class OrganizerTourDetailRuForm(forms.ModelForm):

    title_ru = forms.CharField(label='Tour Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_ru = forms.CharField(label='Text in Russian',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TourDetailRU
        fields = ('title_ru', 'text_ru', )



class OrganizerTourImageForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo', widget = forms.ClearableFileInput(attrs={
        'class' : 'photo-input'
    }))

    class Meta:
        model = TourImage
        fields = ('image', )

class OrganizerTourScheduleForm(forms.ModelForm):

    schedule_image = forms.FileField(label = 'Select Schedule', widget = forms.ClearableFileInput(attrs={
        'class' : 'schedule-input'
    }))

    class Meta:
        model = TourSchedule
        fields = ('schedule_image', )

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
        fields = [ 'title','city','country','address','guide','descriptionen','descriptionaz','descriptionru', 'activity_type', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', 'map_link']

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
            }),
             'map_link' : forms.URLInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Add Map link here'
            })
        }
    

class OrganizerActivityDetailEnForm(forms.ModelForm):

    title_en = forms.CharField(label='Activity Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_en = forms.CharField(label='Text in English',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))

    class Meta:
        model = ActivityDetailEN
        fields = ('title_en', 'text_en', )

class OrganizerActivityDetailAzForm(forms.ModelForm):

    title_az = forms.CharField(label='Activity Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_az = forms.CharField(label='Text in Azerbaijan',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))

    class Meta:
        model = ActivityDetailEN
        fields = ('title_az', 'text_az', )


class OrganizerActivityDetailRuForm(forms.ModelForm):

    title_ru = forms.CharField(label='Activity Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_ru = forms.CharField(label='Text in Russian',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))

    class Meta:
        model = ActivityDetailEN
        fields = ('title_ru', 'text_ru', )

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

    schedule_image = forms.FileField(label = 'Select Schedule', widget = forms.ClearableFileInput(attrs={
        'class' : 'schedule-input'
    }))

    class Meta:
        model = ActivitySchedule
        fields = ('schedule_image', )


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

    start_hour = forms.TimeField(widget = forms.TimeInput(attrs={
        'class' : 'form-input',
        'type' : 'time'
    }), required=False)

    finish_hour = forms.TimeField(widget = forms.TimeInput(attrs={
        'class' : 'form-input',
        'type' : 'time'
    }), required=False)

    # guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    descriptionen = forms.CharField(label = 'Training Description in English', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    descriptionaz = forms.CharField(label = 'Training Description in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    descriptionru = forms.CharField(label = 'Training Description in Russia', widget = forms.Textarea(attrs = {'class': 'form-input', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    
    class Meta:
        model = Training
        fields = ['title', 'descriptionen','descriptionaz','descriptionru', 'training_type', 'country', 'city','address', 'price', 'pricefor', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'start_hour', 'finish_hour', 'avatar', 'cover', 'trainer','map_link']

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
            }),
            'trainer' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Who is trainer?'
            }),
             'map_link' : forms.URLInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Add Map link here'
            })
        }


class OrganizerTrainingDetailEnForm(forms.ModelForm):
    title_en = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_en = forms.CharField(label='Text in English',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TrainingDetailEN
        fields = ('title_en', 'text_en', )


class OrganizerTrainingDetailAzForm(forms.ModelForm):
    title_az = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_az = forms.CharField(label='Text in Azerbaijan',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TrainingDetailEN
        fields = ('title_az', 'text_az', )


class OrganizerTrainingDetailRuForm(forms.ModelForm):
    title_ru = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
    text_ru = forms.CharField(label='Text in Russian',widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
    
    class Meta:
        model = TrainingDetailEN
        fields = ('title_ru', 'text_ru', )

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

    schedule_image = forms.FileField(label = 'Select Schedule', widget = forms.ClearableFileInput(attrs={
        'class' : 'schedule-input'
    }))

    class Meta:
        model = TrainingSchedule
        fields = ('schedule_image', )


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



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("first_name", 'last_name','email', 'phone_number', 'message',)

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Enter First Name'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Enter Last Name'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Enter Email'
            }),
            'phone_number' : forms.TextInput(attrs={
                'class' : 'form-input',
                'id' : 'phone',
                'type' : 'tel'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-input',
                'placeholder' : 'Message...',
                'rows' : '5'
            })
        }

