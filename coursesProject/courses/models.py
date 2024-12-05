from django.db import models

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=25)
  long_description = models.TextField(max_length=150)
  photo = models.ImageField(upload_to='courses/images')