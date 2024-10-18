from django.shortcuts import render, get_object_or_404
from .models import Player
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'home.html')

class PlayerListView(ListView):
    model = Player
    template_name = 'players/player_list.html'
    context_object_name = 'players'
    ordering = ['name']
    paginate_by = 10 

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'
    context_object_name = 'player'

    def get_object(self):
        return get_object_or_404(Player, pk=self.kwargs.get('pk'))