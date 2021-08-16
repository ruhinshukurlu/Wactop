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
from ckeditor_uploader.widgets import CKEditorUploadingWidget



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
            'certification' : forms.FileInput(attrs={
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
            'certification' : forms.FileInput(attrs={
                'class' : 'form-input',
            })
        }


class OrganizerPhotoEditForm(forms.ModelForm):

    image = forms.FileField(label = 'Select Photo')

    class Meta:
        model = TrainingImage
        fields = ('image', )


# Tour app
class OrganizerTourForm(forms.ModelForm):
    title = forms.CharField(label='Tour Title', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Enter Title'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Country...'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'City...'}))

    datefrom = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }), required=False)
    dateto = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }), required=False)

    guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    description_en = forms.CharField(
        label = 'Tour Description in Engilsh',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about tour...', 'rows' : '5'}))
    description_az = forms.CharField(
        label = 'Tour Description in Azerbaijan',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about tour...', 'rows' : '5'}),
        required = False)
    description_ru = forms.CharField(
        label = 'Tour Description in Russia',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about tour...', 'rows' : '5'}),
        required=False)

    class Meta:
        model = Tour
        fields = [ 'title','city','country','address','guide','description_en', 'description_az', 'description_ru', 'tour_type', 'price', 'pricefor','discount', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', 'map_link']

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




# class OrganizerTourDetailForm(forms.ModelForm):

#     title_en = forms.CharField(
#         label='Tour Paragraph',
#         widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))

#     text_en = forms.CharField(
#         label='Text in English',
#         widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))

#     title_az = forms.CharField(
#         label='Tour Paragraph',
#         widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}), required=False)

#     text_az = forms.CharField(
#         label='Text in Azerbaijan',
#         widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}), required=False)

#     title_ru = forms.CharField(
#         label='Tour Paragraph',
#         widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}), required=False)

#     text_ru = forms.CharField(
#         label='Text in Russian',
#         widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}), required=False)

#     class Meta:
#         model = TourDetail
#         fields = ('title_en', 'text_en', 'title_az', 'text_az', 'title_ru', 'text_ru', )



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


#Activity app
class OrganizerActivityForm(forms.ModelForm):
    title = forms.CharField(label='Activity Title', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Enter Title'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Country...'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'City...'}))

    datefrom = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }), required=False)
    dateto = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }), required=False)

    guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    description_en = forms.CharField(
        label = 'Activity Description in English',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about activity...', 'rows' : '5'}))
    description_az = forms.CharField(
        label = 'Activity Description in Azerbaijan',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about activity...', 'rows' : '5'}),
        required =False)
    description_ru = forms.CharField(
        label = 'Activity Description in Russia',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about activity...', 'rows' : '5'}),
        required=False)

    class Meta:
        model = Activity
        fields = [ 'title','city','country','address','guide','description_en','description_az','description_ru', 'activity_type', 'price', 'pricefor', 'currency','discount', 'durationday', 'durationnight', 'datefrom', 'dateto', 'avatar', 'cover', 'map_link']

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
            'discount' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Discount'
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


# class OrganizerActivityDetailForm(forms.ModelForm):

#     title_en = forms.CharField(
#         label='Activity Paragraph',
#         widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
#     text_en = forms.CharField(
#         label='Text in English',
#         widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
#     title_az = forms.CharField(
#         label='Activity Paragraph',
#         widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}), required=False)
#     text_az = forms.CharField(
#         label='Text in Azerbaijan',
#         widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}), required=False)
#     title_ru = forms.CharField(
#         label='Activity Paragraph',
#         widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}), required=False)
#     text_ru = forms.CharField(
#         label='Text in Russian',
#         widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}), required=False)

#     class Meta:
#         model = ActivityDetail
#         fields = ('title_en', 'text_en', 'title_az', 'text_az', 'title_ru', 'text_ru', )


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

#Training app
class OrganizerTrainingForm(forms.ModelForm):
    title = forms.CharField(label='Tour Title', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Enter Title'}))
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'Country...'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-input','placeholder' : 'City...'}))

    datefrom = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }), required=False)
    dateto = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-input',
        'type' : 'date'
    }), required=False)

    start_hour = forms.TimeField(widget = forms.TimeInput(attrs={
        'class' : 'form-input',
        'type' : 'time'
    }))

    finish_hour = forms.TimeField(widget = forms.TimeInput(attrs={
        'class' : 'form-input',
        'type' : 'time'
    }))

    # guide = forms.CharField(label = 'Guide', widget = forms.TextInput(attrs = {'class' : 'form-input', 'placeholder' : 'Who is tour guide?'}))
    description_en = forms.CharField(
        label = 'Training Description in English',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}))
    description_az = forms.CharField(
        label = 'Training Description in Azerbaijan',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}),
        required=False)
    description_ru = forms.CharField(
        label = 'Training Description in Russia',
        widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about training...', 'rows' : '5'}),
        required=False)

    class Meta:
        model = Training
        fields = ['title', 'description_en','description_az','description_ru', 'training_type', 'country', 'city','address', 'price', 'pricefor','discount', 'currency', 'durationday', 'durationnight', 'datefrom', 'dateto', 'start_hour', 'finish_hour', 'avatar', 'cover', 'trainer','map_link']

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
            'discount' : forms.NumberInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Discount'
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


# class OrganizerTrainingDetailForm(forms.ModelForm):

#     title_en = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}))
#     text_en = forms.CharField(label='Text in English', widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}))
#     title_az = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}), required=False)
#     text_az = forms.CharField(label='Text in Azerbaijan', widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}), required=False)
#     title_ru = forms.CharField(label='Training Paragraph', widget=forms.TextInput(attrs={'class': 'form-input mb-2','placeholder' : 'Enter Paragraph Title'}), required=False)
#     text_ru = forms.CharField(label='Text in Russian', widget = forms.Textarea(attrs = {'class': 'form-input mb-2', 'placeholder' : 'Enter your custom paragraph here...', 'rows' : '5'}), required=False)

#     class Meta:
#         model = TrainingDetail
#         fields = ('title_en', 'text_en', 'title_az', 'text_az', 'title_ru', 'text_ru', )


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

    description = forms.CharField(label = 'Description', widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about organizer...', 'rows' : '5'}))
    about = forms.CharField(label = 'Description', widget = forms.Textarea(attrs = {'class': 'form-input ckeditor', 'placeholder' : 'Enter short description about organizer...', 'rows' : '5'}))

    class Meta:
        model = Organizer
        fields = ['organizer_name', 'email', 'description', 'organizer_type', 'about', 'website', 'facebook', 'instagram', 'address', 'contact_number_1', 'contact_number_2', 'profile_photo', 'cover']

        widgets = {
            'organizer_type' : forms.Select(attrs={
                'class' : 'custom-select'
            }),
            # 'description' : forms.Textarea(attrs={
            #     'class': 'form-input ckeditor',
            #     'placeholder' : 'Enter short description about organizer...',
            #     'rows' : '5'
            # }),
            # 'about' : forms.Textarea(attrs={
            #     'rows' : '5'
            # }),
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


class OrganizerAdminForm(forms.ModelForm):
    desciption = forms.CharField(widget=CKEditorUploadingWidget())
    about = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Organizer
        fields = '__all__'
