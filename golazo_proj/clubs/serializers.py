from rest_framework import serializers
from .models import Club
from players.models import Player


class PlayerNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'value', 'goals', 'assists', 'age', 'photo']  # Include only essential fields


class ClubSerializer(serializers.ModelSerializer):
    players = PlayerNestedSerializer(many=True, read_only=True)  # Use the lightweight serializer

    class Meta:
        model = Club
        fields = '__all__'
