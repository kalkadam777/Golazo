from rest_framework import serializers
from .models import League, Match, Standings

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class StandingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standings
        fields = '__all__'