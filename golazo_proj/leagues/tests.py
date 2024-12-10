from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import League, Match, Standings
from clubs.models import Club
from django.contrib.auth.models import User, Group
from datetime import date

class LeagueAPITestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='admin123')
        self.admin_group = Group.objects.create(name='League Admin')
        self.admin_user.groups.add(self.admin_group)

        self.team_manager = User.objects.create_user(username='manager', password='manager123')
        self.team_group = Group.objects.create(name='Team Manager')
        self.team_manager.groups.add(self.team_group)

        self.client = APIClient()

        self.club1 = Club.objects.create(name="Real Madrid", value=1000000000, country="ES", league="La Liga")
        self.club2 = Club.objects.create(name="Barcelona", value=900000000, country="ES", league="La Liga")

        self.league = League.objects.create(
            name="La Liga",
            country="Spain",
            start_date=date(2023, 8, 1),
            end_date=date(2024, 5, 15),
        )

        if not Standings.objects.filter(club=self.club1).exists():
            self.standings = Standings.objects.create(
                league=self.league,
                club=self.club1,
                matches_played=1,
                wins=1,
                draws=0,
                losses=0,
                goals_scored=2,
                goals_conceded=1,
                points=3,
            )

        if not Standings.objects.filter(club=self.club2).exists():
            Standings.objects.create(
                league=self.league,
                club=self.club2,
                matches_played=0,
                wins=0,
                draws=0,
                losses=0,
                goals_scored=0,
                goals_conceded=0,
                points=0,
            )

        self.match = Match.objects.create(
            league=self.league,
            home_team=self.club1,
            away_team=self.club2,
            home_team_score=2,
            away_team_score=1,
            match_date=date(2023, 9, 10),
        )

        self.league_url = reverse('league-list')
        self.match_url = reverse('match-list')
        self.standings_url = reverse('standings-list')

    def test_get_league_list(self):
        response = self.client.get(self.league_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.league.name)

    def test_get_match_list(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.match_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['home_team'], self.club1.pk)

    def test_get_standings_list(self):
        response = self.client.get(self.standings_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['points'], self.standings.points)

    def test_create_match_unauthorized(self):
        data = {
            "league": self.league.pk,
            "home_team": self.club1.pk,
            "away_team": self.club2.pk,
            "home_team_score": 1,
            "away_team_score": 1,
            "match_date": date(2023, 9, 17),
        }
        response = self.client.post(self.match_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_match_authorized(self):
        self.client.force_authenticate(user=self.admin_user)
        data = {
            "league": self.league.pk,
            "home_team": self.club1.pk,
            "away_team": self.club2.pk,
            "home_team_score": 1,
            "away_team_score": 1,
            "match_date": date(2023, 9, 17),
        }
        response = self.client.post(self.match_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.count(), 2)

    def test_permissions_for_non_admin(self):
        self.client.force_authenticate(user=self.team_manager)
        response = self.client.post(self.match_url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
