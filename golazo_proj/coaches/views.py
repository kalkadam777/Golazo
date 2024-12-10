from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Manager
from .serializers import ManagerSerializer


class ManagerListView(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    

class ManagerDetailView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
    
class ManagerCreateView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
    
class ManagerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
    
class ManagerDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    
