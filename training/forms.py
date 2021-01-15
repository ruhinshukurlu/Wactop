from django import forms
from django.forms import ModelForm
from training.models import Comment, TrainingDeny


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

