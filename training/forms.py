from django import forms
from django.forms import ModelForm
from training.models import Comment, TrainingDeny, Training, TrainingDetail
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('rating', 'message',)
        widgets={
            'message': forms.Textarea(attrs={
                'class': 'form-input resize',
                'placeholder' : 'Write Comment...',
                'rows' : '5'    
            }),         
        }


class TrainingDenyForm(forms.ModelForm):
    
    class Meta:
        model = TrainingDeny
        fields = ("message",)
        widgets={
            'message': forms.Textarea(attrs={
                'class': 'form-input resize',
                'placeholder' : 'Write Comment...',
                'rows' : '5'    
            }),            
        }


class TrainingAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Training
        fields = '__all__'


class TrainingDetailAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TrainingDetail
        fields = '__all__'


