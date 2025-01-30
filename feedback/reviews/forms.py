from django import forms
from .models import Review, Novell

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Your name",required=True,max_length=10,error_messages={
#     'required':'O campo non pode quedar baleiro',
#     'max_length': f'O campo non pode ter máis de 10 caracteres o teu ten'
#   })
#   review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
#   rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
  
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
    
#EXEMPLO do uso de widgets no modelform
class SmartPhoneForm(forms.ModelForm):
  class Meta:
        model = Phone
        fields = ['smart_phone_ownership', 'smart_phone_usage']
        widgets = {
            'smart_phone_ownership': forms.RadioSelect,
            'smart_phone_usage': forms.Select,
        }
        
class NovellForm(forms.ModelForm):
  class Meta: 
    model = NovellForm
    fields = '__all__'
    widgets = {
      'role': forms.RadioSelect,
      'sign_in': forms.CheckboxSelectMultiple
    }