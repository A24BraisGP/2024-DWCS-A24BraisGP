from django.shortcuts import render
from .models import Game, Detail
# Create your views here.
def home(request):
  games = Game.objects.all().order_by('title')

  if request.GET.get('filter') and request.GET.get('filter')!= 'All':      
    game_filter = request.GET.get('filter')
    games = Game.objects.filter(diversity=game_filter)
  
  return render(request,'catalogo/home.html',{'games':games})