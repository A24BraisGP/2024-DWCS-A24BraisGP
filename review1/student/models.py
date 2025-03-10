from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(unique=True,blank=True)
    year_of_birth = models.IntegerField(validators=[MinValueValidator(1970),MaxValueValidator(2010)],null=True, blank=True)
    finished_degree = models.BooleanField(default=False)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True, related_name='degrees')
    
    def get_absolute_url(self):
        return reverse("student-detail", kwargs={self.slug})
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name_surname)
        super().save(*args,**kwargs)
        
    def __str__(self):
        return self.name_surname
    
# from student.models import Degree,Student 
# degree = Degree.objects.get(id=1)
# students = Student.objects.all()
# student_older_20 = students.filter(year_of_birth__lte=2005)
# student_older_25_finished = students.filter(year_of_birth__lte=2005, finished_degree=True)
# from django.db.models import Avg
# avg_year = students.aggregate(Avg('year_of_birth'))
# {'year_of_birth__avg': 2002.0}
# avg_age = 2025 - avg_year['year_of_birth__avg']

# students_degree = Student.objects.all().filter(finished_degree = True).count()

# students_finished_degree = Student.objects.filter(degree=degree, finished_degree=True)
