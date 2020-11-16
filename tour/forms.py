from django import forms
from django.forms import ModelForm
from tour.models import TourComment


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