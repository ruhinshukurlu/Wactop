from django import forms
from django.forms import ModelForm
from activity.models import ActivityComment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = ActivityComment
        fields = ('rating', 'message',)
        widgets={
            'message': forms.Textarea(attrs={
                'class': 'form-input resize',
                'placeholder' : 'Write Comment...',
                'rows' : '5'    
            }),         
        }
