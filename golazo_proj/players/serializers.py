from rest_framework import serializers
from .models import Player, TransferHistory
from clubs.serializers import ClubSerializer

class PlayerSerializer(serializers.ModelSerializer):
    current_club = ClubSerializer()
    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'value', 'country', 'goals', 'assists', 'age', 'photo', 'current_club']

class TransferHistorySerializer(serializers.ModelSerializer):
    player = serializers.StringRelatedField()
    club = serializers.StringRelatedField()
    

    class Meta:
        model = TransferHistory
        fields = '__all__'