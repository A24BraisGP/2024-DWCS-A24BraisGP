from django import forms
from .models import Review, Student

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

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'
    labels ={
      'name' : 'Name',
      'degree' : 'Degree'
    }
    error_messages = {
      'name':{
          'required':'O campo é requerido',
          'max_length':'Pasacheste de largo'
      },
      'degree':{
          'required':'O campo é requerido',
          'max_length':'Pasacheste de largo'
      }
    }