from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Review(models.Model):
  user_name = models.CharField(max_length=10)
  review_text = models.TextField()
  rating = models.IntegerField(validators=[MaxValueValidator(10)])
  
class Student (models.Model):
  name = models.CharField(max_length=100)
  degree = models.CharField(max_length=100)
  