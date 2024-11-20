from django.db import models

# Create your models here.
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
  trailer_url = models.URLField(blank=True)