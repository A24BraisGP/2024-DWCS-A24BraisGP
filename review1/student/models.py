from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from datetime import date
# Create your models here.
class Degree(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350)
    number_of_years = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(4)])
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name_surname = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='alumni')
    age = models.DateField(validators=[MinValueValidator(date(1970,1,1)),MaxValueValidator(date(2010,1,1))])
    slug = models.SlugField(unique=True,blank=True)
    finished_degree = models.BooleanField(default=False)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True)
    
    def get_absolute_url(self):
        return reverse("student-detail", kwargs={self.slug})
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name_surname)
        super().save(*args,**kwargs)