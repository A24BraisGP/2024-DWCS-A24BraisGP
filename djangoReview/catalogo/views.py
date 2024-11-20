from django.shortcuts import render
from .models import Game, Opinion
# Create your views here.
def home(request):
  games = Game.objects.all()
  opinions = Opinion.objects.all() 
  return render(request,'catalogo/home.html',{'games':games})