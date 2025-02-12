from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['user_name', 'user_email','text']
        labels = {
            'user_name': 'User Name: ',
            'user_email': 'Your Email: ',
            'text': 'Leave your comment!'
        }
        error_messages = {
            'user_name':{
                'required': 'Your name must be filled',
                'max_length': 'Your name was too long'
            }
        }