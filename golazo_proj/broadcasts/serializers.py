from rest_framework import serializers
from .models import LiveBroadcast

class BroadcastSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = LiveBroadcast 
        fields = '__all__'