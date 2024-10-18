from rest_framework import serializers
from .models import PlayerStatistics

class PlayerStatisticsSerializer(serializers.ModelSerializer):
    player = serializers.StringRelatedField()

    class Meta:
        model = PlayerStatistics
        fields = '__all__'