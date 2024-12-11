from django.shortcuts import render
from .models import LiveBroadcast
from .serializers import BroadcastSerializer
from rest_framework import generics

# Create your views here.
class BroadcastListView(generics.ListAPIView): 
    queryset = LiveBroadcast.objects.all() 
    serializer_class = BroadcastSerializer 
     
class BroadcastDetailView(generics.RetrieveAPIView): 
    queryset = LiveBroadcast.objects.all() 
    serializer_class = BroadcastSerializer 
     
class BroadcastCreateView(generics.CreateAPIView): 
    queryset = LiveBroadcast.objects.all() 
    serializer_class = BroadcastSerializer 
     
class BroadcastUpdateView(generics.RetrieveUpdateAPIView): 
    queryset = LiveBroadcast.objects.all() 
    serializer_class = BroadcastSerializer 
     
class BroadcastDeleteView(generics.RetrieveDestroyAPIView): 
    queryset = LiveBroadcast.objects.all() 
    serializer_class = BroadcastSerializer