from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    data = models.DateField()
    description = models.TextField()