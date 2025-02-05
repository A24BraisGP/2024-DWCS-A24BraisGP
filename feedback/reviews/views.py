from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm, StudentForm
from .models import Review, Student
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
import random
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView,DeleteView

# Create your views here.

# class ReviewView(FormView):
#   form_class = ReviewForm
#   template_name = 'reviews/review.html'
#   success_url = '/thank_you'
  
#   def form_valid(self, form):
#       form.save()
#       return super().form_valid(form)

# Garda automaticamente na base de datos cando temos un model Form
class ReviewView(CreateView):
  model = Review
  form_class = ReviewForm
  template_name = 'reviews/review.html'
  success_url = '/thank_you'
  
class ThankYouView(TemplateView):
  template_name = 'reviews/thank_you.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    message = 'This works!'
    context["message"] = message
    print(context)
    return context

class ReviewListView(ListView):
  template_name = 'reviews/review_list.html'
  model = Review
  context_object_name = "review_list"

  # se queremos ordear a listaxe de obxectos traidos pela listview
  
  def get_queryset(self):
    base_query =  super().get_queryset()
    data = base_query.order_by('-rating')
    return data
  
class SingleReviewView(DetailView):
  template_name = 'reviews/single_review.html'
  model = Review
  
  #por ser queremos cambialo nome do obxecto que pasamos 
  
  context_object_name = 'review'
  
  # def get_context_data(self, **kwargs):
  #     objectId = kwargs['id']
  #     context = super().get_context_data(**kwargs)
  #     review = get_object_or_404(Review, id=objectId)
  #     context["single_review"] = review
  #     return context


class StudentView(CreateView):
  model = Student
  form_class = StudentForm
  template_name = 'reviews/student.html'
  success_url = '/student_list'
  
  
  
class StudentList(ListView):
  template_name = 'reviews/student_list.html'
  model = Student
  context_object_name = 'student_list'
  
  def get_queryset(self):
    base_query =  super().get_queryset()
    data = base_query.order_by('name')
    return data
  
class StudentUpdate(UpdateView):
  model = Student
  fields = ['name', 'degree']
  template_name = 'reviews.student_update.html'
  success_url = ''  
  
  
class StudentDelete(DeleteView):
  model = Student
  success_url = 'reviews/student_deleted.html'