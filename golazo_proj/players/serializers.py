from rest_framework import serializers
from .models import Player, TransferHistory

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TransferHistorySerializer(serializers.ModelSerializer):
    player = serializers.StringRelatedField()
    club = serializers.StringRelatedField()

    class Meta:
        model = TransferHistory
        fields = '__all__'