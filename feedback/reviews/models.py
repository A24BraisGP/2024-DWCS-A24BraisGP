from django.db import models

# Create your models here.
class Review(models.Model):
  user_name = models.CharField(max_length=10)
  review_text = models.TextField()
  rating = models.IntegerField()
  
class Novell(models.Model):
  SERVER_CHOICES =(
    ('Apache','Apache'),
    ('Nginx','Nginx'),
    ('GoogleCloud','Google Cloud'),
  )
  
  ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Engineer', 'Engineer'),
    ('Manager', 'Manager'),
    ('Guest', 'Guest')
  )
  
  SIGN_CHOICES = (
    ('Mail', 'Mail'),
    ('Payroll', 'Payroll'),
    ('Self-Service', 'Self-Service')
  )
  
  user_name = models.CharField(label="Username: ",required=True,max_length=10)
  password = models.CharField(label='Password',max_length=32,widget=models.PasswordInput)
  city = models.CharField(label='City of Employment: ')
  web_server = models.ChoiceField(choices = SERVER_CHOICES)
  role = models.ChoiceField(choices = ROLE_CHOICES)
  sing_in = models.ChoiceField(choices = SIGN_CHOICES)