from django import forms
from django.forms import ModelForm
from activity.models import ActivityComment, ActivityDeny


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


class ActivityDenyForm(forms.Form):
    message = forms.CharField(widget = forms.Textarea(attrs={
                'class': 'form-input resize',
                'placeholder' : 'Write Comment...',
                'rows' : '5'    
            }), required=True) 


    
