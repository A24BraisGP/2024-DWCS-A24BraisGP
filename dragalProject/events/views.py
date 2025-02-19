from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from .models import Event,Game
from django.views.generic import ListView
from .forms import EventForm
from django.urls import reverse_lazy

# Create your views here
class HomeView(TemplateView):
   template_name = 'events/home.html'
   
   
   def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['events'] = Event.objects.all()
      return context

class AllEventView(ListView):
   pass
class CreateEventView(View):
   def post(self,request):
      model = Event
      form_class = EventForm
      template_name = 'events/create_event.html'
      success_url = reverse_lazy('create-event')
      
      
   def get(self,request):
      pass