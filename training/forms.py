from django import forms
from django.forms import ModelForm
from training.models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('rating', 'message',)
        widgets={
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Name'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Message'}),            
        }
