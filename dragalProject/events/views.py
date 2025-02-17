from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Event,Game
from django.views.generic import ListView


# Create your views here
class HomeView(TemplateView):
   template_name = 'events/home.html'
   
   
   def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)
      context['events'] = Event.objects.all()
      return context

class AllEventView(ListView):
   pass
class EventView(CreateView):
   pass

