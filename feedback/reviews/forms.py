from django import forms
from .models import Review, Novell

class ReviewForm(forms.ModelForm):
  class Meta: 
    model = Review
    fields = '__all__'
    # fields = ['user_name',...]
    # exclude = ['']
    labels = {
      'user_name' : 'Username:',
      'review_text' : 'Your Review',
      'rating' : 'Your Rating'
    }
    error_messages ={
      'user_name':{
        'required':'O campo é requerido',
        'max_length':'Pasacheste de largo'
      }
    }

class NovellForm(forms.ModelForm):
  class Meta: 
    model = Novell
    fields = '__all__'
    labels={
      'user_name' : 'User name',
      'password': 'Password',
      'city': 'City',
      'web_server': 'Web Server',
      'role': 'Role',
    }
    widgets = {
      'password': forms.PasswordInput,
      'role': forms.RadioSelect,
      'sign_in': forms.CheckboxSelectMultiple
    }