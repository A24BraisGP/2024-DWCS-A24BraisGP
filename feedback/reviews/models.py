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
  
  user_name = models.CharField(max_length=10)
  password = models.CharField(max_length=32)
  city = models.CharField(max_length=20)
  web_server = models.CharField(max_length=200,choices = SERVER_CHOICES)
  role = models.CharField(max_length=200,choices = ROLE_CHOICES)