from django import forms
from django.forms import ModelForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from tour.models import TourComment , TourDeny , Tour


class TourCommentForm(forms.ModelForm):

    class Meta:
        model = TourComment
        fields = ('rating', 'message',)
        widgets={
            'message': forms.Textarea(attrs={
                'class': 'form-input resize',
                'placeholder' : 'Write Comment...',
                'rows' : '5'
            }),
        }


class TourDenyForm(forms.ModelForm):

    class Meta:
        model = TourDeny
        fields = ("message",)
        widgets={
            'message': forms.Textarea(attrs={
                'class': 'form-input resize',
                'placeholder' : 'Write Comment...',
                'rows' : '5'
            }),
        }


class TourAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Tour
        fields = '__all__'


# class TourDetailAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = TourDetail
#         fields = '__all__'
