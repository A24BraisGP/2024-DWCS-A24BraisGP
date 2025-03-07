from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    price = models.FloatField(blank=True)
    picture = models.ImageField(upload_to='products')
    slug = models.SlugField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)    
        super().save(self,**kwargs)
        
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={self.slug})
    