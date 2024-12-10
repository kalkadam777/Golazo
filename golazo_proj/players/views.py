from django.shortcuts import render, get_object_or_404
from .models import Player
from django.views.generic import ListView, DetailView
from django.db.models import Q
from rest_framework import generics
from .serializers import PlayerSerializer
from .pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


def home(request):
    valuable_players = Player.objects.order_by('-value')[:5]  
    young_players = Player.objects.order_by('age')[:5] 
    context = {
        'valuable_players': valuable_players,
        'young_players': young_players,
    }
    return render(request, 'home.html', context)

class ValuablePlayersList(generics.ListAPIView):
    queryset = Player.objects.order_by('-value')[:5]  
    serializer_class = PlayerSerializer
    
    
class YoungPlayersListView(generics.ListAPIView):
    queryset = Player.objects.order_by('age')[:5] 
    serializer_class = PlayerSerializer
    

class PlayerListView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'position': ['exact'],
        'value': ['gte', 'lte'],
    }
    search_fields = ['name', 'position']
    ordering_fields = ['value', 'age', 'name']
    ordering = ['-value']
    
class PlayerDetailView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    
class PlayerCreateView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    
class PlayerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    
class PlayerDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer