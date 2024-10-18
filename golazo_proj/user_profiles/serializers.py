from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    favorite_players = serializers.StringRelatedField(many=True)
    favorite_clubs = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'