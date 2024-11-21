from django.shortcuts import render
from .models import Game, Detail
# Create your views here.
def home(request):
  games = Game.objects.all()
  return render(request,'catalogo/home.html',{'games':games})