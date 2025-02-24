from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Event, Artist
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
        
        if self.request.GET.get('filter'):
            event_filter = self.request.GET.get('filter')
            events = self.filter_events(event_filter)
            context["events"] = events
        return context
    
    def filter_events(self, event_filter):
        events = Event.objects.all()
        if event_filter == "price":
            events.order_by("ticket_price")
        elif event_filter == "date":
            events.order_by("date")
        elif event_filter == "city":
            events.order_by("city")
            
        return events[:3]
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
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        event = context['event']
        cart = self.request.session.get('cart')
        is_in_cart = False
        if cart is None:
            is_in_cart = False
        else:
            is_in_cart = event.id in cart
        context['in_cart'] = is_in_cart
        return context
    
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
        cart = request.session.get('cart')
        if cart is None or len(cart) == 0:
            cart = []
        event_id = int(request.POST['event_id'])
        if event_id not in cart: 
            cart.append(event_id)
        else:
            cart.remove(event_id)          
        request.session['cart'] = cart            
        events = Event.objects.filter(id__in=cart)
        total_price = 0
        for event in events:
            total_price += event.ticket_price
        request.session['total_price'] = total_price
        print(request.session['total_price'])
        return HttpResponseRedirect("/")
    
    def get(self,request):
        cart = request.session.get('cart')
        total_price = request.session.get('total_price')
        context = {}
        if cart is None or len(cart) == 0:
            context['events'] = []
            context['has_cart'] = False
            context['total_price'] = 0 
        else:
            events = Event.objects.filter(id__in=cart)
            context['events'] = events
            context['has_cart'] = True
            context['total_price'] = total_price
            
        return render(request, 'events/cart.html',context)

class ArtistDetailView(DetailView):
    template_name = 'events/artist_detail.html'
    model = Artist
    context_object_name = 'artist'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = context['artist']
        song_list = artist.songs
        songs = song_list.split(', ')
        context['songs'] = songs
        return context
    