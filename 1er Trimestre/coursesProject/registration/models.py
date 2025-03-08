from django.core.validators import MinValueValidator as min_val
from django.db import models

# Create your models here.
class Registration(models.Model):
  name = models.CharField(max_length=25)
  surname = models.CharField(max_length=25)
  age = models.IntegerField(validators=[min_val(12)])