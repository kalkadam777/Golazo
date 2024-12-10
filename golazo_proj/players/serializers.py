from rest_framework import serializers
from .models import Player, TransferHistory
from clubs.models import Club

class ClubNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'value', 'country', 'emblem', 'league']  # Include only essential fields


class PlayerSerializer(serializers.ModelSerializer):
    current_club = ClubNestedSerializer(read_only=True)  # Use the lightweight serializer

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'value', 'country', 'goals', 'assists', 'age', 'photo', 'current_club']


class TransferHistorySerializer(serializers.ModelSerializer):
    player = serializers.StringRelatedField()
    club = serializers.StringRelatedField()
    
    class Meta:
        model = TransferHistory
        fields = '__all__'