from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
  caption = models.CharField( max_length=20)
  
  def __str__(self):
    return f'{self.caption}'
  
class Author(models.Model):
  first_name = models.CharField( max_length=100)
  last_name = models.CharField( max_length=100)
  email_addres = models.EmailField( max_length=254)
  
  def __str__(self):
    return f'{self.first_name} - {self.last_name} - {self.email_addres}'
  
class Post(models.Model):
  title = models.CharField( max_length=50)
  excerpt = models.CharField( max_length=50)
  image = models.ImageField(upload_to='posts',null=True)
  date = models.DateField(auto_now_add=True)
  slug = models.SlugField(unique=True, db_index=True)
  content = models.TextField(null=True,validators=[MinLengthValidator(10)])
  author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='fkposts')
  tags = models.ManyToManyField(Tag)
  
  def __str__(self):
    return f'{self.title} - {self.date} - {self.author} \n {self.content}'
  
  def get_absolute_url(self):
      return reverse("post-detail",args=[self.slug])
  