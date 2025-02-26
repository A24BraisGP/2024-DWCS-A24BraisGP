from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='artists')
    songs = models.TextField(max_length=400)

    def __str__(self):
        return self.name 
    
    
    def get_absolute_url(self):
         return reverse("artist-detail", args=[self.pk])
     
class Event(models.Model):
    title = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    date = models.DateField()
    logo = models.ImageField(upload_to='logos',blank=True,null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True,related_name='events')
    slug = models.SlugField(unique=True,blank=True)
    description = models.TextField(max_length=250)
    ticket_price = models.FloatField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.city = self.city.upper()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("event-detail", args={self.slug})
    
    