from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Opinion(models.Model):
  score = models.IntegerField(
    validators=[
      MinValueValidator(1),
      MaxValueValidator(10)
    ]
  )
  description = models.TextField(blank=True, max_length=1500)
  
  
class Game(models.Model):
  VISUAL = "VI"
  MOTOR = "MO"
  COGNITIVE = "CO"
  HEARING = "HE"
  SENSORY = "SE"
  DIVERSITY_TYPE = [
    (VISUAL, "Visual"),
    (MOTOR, "Motor"),
   (COGNITIVE, "Cognitive"),
    (HEARING, "Hearing"),
    (SENSORY, "Sensory"),
  ]
  title = models.CharField(max_length=500)
  cover = models.ImageField(upload_to='catalogo/images')
  diversity = models.CharField(choices=DIVERSITY_TYPE, default=VISUAL,max_length=10)
  description = models.TextField(max_length=1500)
  opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE, null=True, blank=True)
  trailer_url = models.URLField(blank=True)
  