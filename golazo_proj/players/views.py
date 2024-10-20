from django.shortcuts import render, get_object_or_404
from .models import Player
from django.views.generic import ListView, DetailView
from django.db.models import Q

def home(request):
    valuable_players = Player.objects.order_by('-value')[:5]  
    young_players = Player.objects.order_by('age')[:5] 
    context = {
        'valuable_players': valuable_players,
        'young_players': young_players,
    }
    return render(request, 'home.html', context)

class PlayerListView(ListView):
    model = Player
    template_name = 'players/player_list.html'
    context_object_name = 'players'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(current_club__name__icontains=query)
            )

        position = self.request.GET.get('position')
        if position and position != 'All':
            queryset = queryset.filter(position=position)

        min_value = self.request.GET.get('min_value')
        max_value = self.request.GET.get('max_value')
        if min_value and max_value:
            queryset = queryset.filter(value__gte=min_value, value__lte=max_value)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = Player.POSITION_CHOICES  
        context['min_value'] = self.request.GET.get('min_value', 0)
        context['max_value'] = self.request.GET.get('max_value', 100000000)  
        return context

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'
    context_object_name = 'player'

    def get_object(self):
        return get_object_or_404(Player, pk=self.kwargs.get('pk'))