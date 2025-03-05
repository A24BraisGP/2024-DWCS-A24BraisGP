from django.contrib import admin
from .models import Student, Degree
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name_surname',)}
    list_display = ('name_surname','degree')
    list_filter = ('name_surname',)
    
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Degree)