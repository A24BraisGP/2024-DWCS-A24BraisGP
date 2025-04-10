from django.shortcuts import render, get_object_or_404
from catalogo.models import Game, Detail

# Create your views here.
def detail(request, game_id):
    game = get_object_or_404(Game,pk=game_id)
    detail = Detail.objects.get(pk=game_id)
    return render(request,'detail/details.html',{'game':game, 'detail':detail})