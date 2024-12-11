from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import League, Match, Standings
from .serializers import LeagueSerializer, MatchSerializer, StandingsSerializer
from .permissions import IsLeagueAdmin
import datetime, random, logging

logger = logging.getLogger(__name__)

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated, IsLeagueAdmin]


class StandingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Standings.objects.all()
    serializer_class = StandingsSerializer
    permission_classes = [IsAuthenticated]


@login_required
def league_list(request):
    leagues = League.objects.all()
    return render(request, 'leagues/league_list.html', {'leagues': leagues})


@login_required
def league_detail(request, pk):
    league = get_object_or_404(League, pk=pk)
    standings = league.standings.all()
    matches = league.matches.all()
    
    can_add_match = request.user.has_perm('leagues.add_match')
    can_change_standings = request.user.has_perm('leagues.change_standings')

    return render(request, 'leagues/league_detail.html', {
        'league': league,
        'standings': standings,
        'matches': matches,
        'can_add_match': can_add_match,
        'can_change_standings': can_change_standings,
    })

@login_required
@permission_required('leagues.add_match', raise_exception=True)
def generate_matches(request, pk):
    league = get_object_or_404(League, pk=pk)
    Match.create_matches_for_league(league)
    return redirect('league_detail', pk=league.pk)


@login_required
@permission_required('leagues.change_standings', raise_exception=True)
def update_standings(request, pk):
    league = get_object_or_404(League, pk=pk)
    if request.method == 'POST':
        pass
    return render(request, 'leagues/update_standings.html', {'league': league})


@login_required
@permission_required('leagues.change_standings', raise_exception=True)
def randomize_past_results(request, pk):

    league = get_object_or_404(League, pk=pk)
    target_date = datetime.date(2024, 12, 11)  

    matches_to_update = league.matches.filter(
        match_date__lte=target_date,
        home_team_score=0,
        away_team_score=0
    )

    for match in matches_to_update:
        home_score = random.randint(0, 5)
        away_score = random.randint(0, 5)
        match.home_team_score = home_score
        match.away_team_score = away_score
        match.save()
        match.process_match_result() 

    logger.info(f"Randomized past results for league {league.name} up to {target_date}. Matches updated: {matches_to_update.count()}")
    
    return redirect('league_detail', pk=league.pk)