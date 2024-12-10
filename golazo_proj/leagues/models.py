from django.db import models
from clubs.models import Club
from datetime import timedelta
import itertools
import random


class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    logo = models.ImageField(upload_to='league_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches')
    home_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_matches')
    home_team_score = models.PositiveIntegerField(default=0)
    away_team_score = models.PositiveIntegerField(default=0)
    match_date = models.DateField()

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} ({self.league.name})"

    def process_match_result(self):
        standings_home = self.home_team.standings
        standings_away = self.away_team.standings

        if self.home_team_score > self.away_team_score:
            standings_home.wins += 1
            standings_home.points += 3
            standings_away.losses += 1
        elif self.home_team_score < self.away_team_score:
            standings_away.wins += 1
            standings_away.points += 3
            standings_home.losses += 1
        else:
            standings_home.draws += 1
            standings_away.draws += 1
            standings_home.points += 1
            standings_away.points += 1

        standings_home.matches_played += 1
        standings_away.matches_played += 1
        standings_home.goals_scored += self.home_team_score
        standings_away.goals_scored += self.away_team_score
        standings_home.goals_conceded += self.away_team_score
        standings_away.goals_conceded += self.home_team_score

        standings_home.save()
        standings_away.save()

    @staticmethod
    def create_matches_for_league(league):
        teams = list(league.standings.values_list('club', flat=True))
        match_dates = [league.start_date + timedelta(days=i * 7) for i in range(len(teams) - 1)]

        for home_team, away_team in itertools.permutations(teams, 2):
            if not Match.objects.filter(league=league, home_team_id=home_team, away_team_id=away_team).exists():
                match_date = random.choice(match_dates)
                Match.objects.create(
                    league=league,
                    home_team_id=home_team,
                    away_team_id=away_team,
                    match_date=match_date
                )


class Standings(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='standings')
    club = models.OneToOneField(Club, on_delete=models.CASCADE, related_name='standings')
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.club.name} - {self.points} pts"

    class Meta:
        verbose_name = 'Standing'
        verbose_name_plural = 'Standings'
        ordering = ['-points', '-goals_scored']