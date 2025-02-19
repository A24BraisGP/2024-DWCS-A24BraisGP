from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Game(models.Model):    
    title = models.CharField(max_length=150, null=True)
    hardware = models.CharField(max_length=25)
    cover_art = models.ImageField(upload_to='covers',null=True)
    recommended_age= models.IntegerField(validators=[MinValueValidator(3),MaxValueValidator(18)])
    
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    title = models.CharField(max_length=150)
    city = models.CharField(max_length=50,null=True)
    date = models.DateField(auto_now_add=False)
    logo = models.ImageField(upload_to='logos',null=True)
    # participants = models.JSONField(default=list, blank=True, null=True)
    slug = models.SlugField(default='',blank=True,null=False,db_index=True)
    description = models.TextField(max_length=400,null=True)
    games = models.ManyToManyField(Game)
    
    def get_absolute_url(self):
        return reverse("event_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()
    