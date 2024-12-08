from django.db.models import Q
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Club
from players.models import Player  
from rest_framework import generics
from .serializers import ClubSerializer

class ClubListView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    ordering = ['name']


class ClubDetailView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    
    
class ClubCreateView(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    

class ClubUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
