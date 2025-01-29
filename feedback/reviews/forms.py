from django import forms
import datetime

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="Your name",required=True,max_length=10,error_messages={
    'required':'O campo non pode quedar baleiro',
    'max_length': f'O campo non pode ter máis de 10 caracteres o teu ten'
  })
  review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
  rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
  
class NovellForm(forms.Form):
  SERVER_CHOICES =(
    ('1','Apache'),
    ('2','Nginx'),
    ('3','Google Cloud'),
  )
  
  ROLE_CHOICES = (
    ('1', 'Admin'),
    ('2', 'Engineer'),
    ('3', 'Manager'),
    ('4', 'Guest')
  )
  
  SIGN_CHOICES = (
    ('1', 'Mail'),
    ('2', 'Payroll'),
    ('3', 'Self-Service')
  )
  
  user_name = forms.CharField(label="Username: ",required=True,max_length=10)
  password = forms.CharField(label='Password',max_length=32,widget=forms.PasswordInput)
  city = forms.DateField(label='City of Employment: ')
  web_server = forms.ChoiceField(choices = SERVER_CHOICES)
  role = forms.ChoiceField( widget=forms.RadioSelect,choices = ROLE_CHOICES)
  sing_in = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices = SIGN_CHOICES)