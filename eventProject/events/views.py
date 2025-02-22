from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Event
from .forms import EventForm
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(TemplateView):
    template_name = 'events/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all().order_by('date')[:3]
        return context
    
class CreateEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = '/'
    
class EventListView(ListView):
    template_name = 'events/list_events.html'
    model = Event
    context_object_name= 'events'
    
    def get_queryset(self):
        base_query = Event.objects.all()
        data = base_query.order_by('date')
        return data
    
class EventDetailView(DetailView):
    template_name = 'events/event_detail.html'
    model = Event
    
class EventDeleteView(DeleteView):
    model = Event
    template_name= 'events/delete_event.html'
    success_url = reverse_lazy('home')
    
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/update_event.html'
    success_url = reverse_lazy('home')

class CartView(View):
    def post(self, request):
        event_id = request.POST['event_id']
        number_tickets = request.POST['numberOfTickets']
        request.session['cart'] = {
             'event_id':event_id,
             'number_tickets':number_tickets   
            } 
        event_slug = Event.objects.get(pk=event_id).slug
        return HttpResponseRedirect("/")
    
    def get(self,request):
        cart = request.session['cart']
        context = {}
        if cart is None:
            context['events'] = []
            context['tickets'] = []
            context['has_cart'] = False
        else:
            events = Event.objects.filter(id__in=cart['event_id'])
            context['events'] = events
            context['tickets'] = []
            context['has_cart'] = True
            
        return render(request, 'events/cart.html',context)
  