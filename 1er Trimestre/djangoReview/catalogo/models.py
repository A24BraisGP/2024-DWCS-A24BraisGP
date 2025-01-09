from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Detail(models.Model):
  score = models.IntegerField(
    validators=[
      MinValueValidator(1),
      MaxValueValidator(10)
    ]
  )
  description = models.TextField(blank=True, max_length=1500)
  #TODO tamén multivaluado
  developer= models.CharField(blank=True, max_length=50)
  developerPage = models.URLField(blank=True)
  # TODO prices táboa con web scraping sobre os prezos dos xogos
  # TODO plataformas es otro atributo multivaluado
  
  
class Game(models.Model):
  VISUAL = "Visual"
  MOTOR = "Motor"
  COGNITIVE = "Cognitive"
  HEARING = "Hearing"
  SENSORY = "Sensory"
  DIVERSITY_TYPE = [
    (VISUAL, "Visual"),
    (MOTOR, "Motor"),
   (COGNITIVE, "Cognitive"),
    (HEARING, "Hearing"),
    (SENSORY, "Sensory"),
  ]
  title = models.CharField(max_length=500)
  cover = models.ImageField(upload_to='catalogo/images')
  #TODO outra táboa para darlle múltiples diversities a cada xogo, xa que unha obra pode cubrir varias accesibilidades.
  diversity = models.CharField(choices=DIVERSITY_TYPE, default=VISUAL,max_length=10)
  description = models.TextField(max_length=150)
  trailer = models.URLField(blank=True)
  