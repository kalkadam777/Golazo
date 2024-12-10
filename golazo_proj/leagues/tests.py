from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import League, Match, Standings
from clubs.models import Club
from django.contrib.auth.models import User, Group

class LeagueAPITestCase(APITestCase):
    def setUp(self):
        # Создание группы "League Admin" для прав
        self.admin_group = Group.objects.create(name="League Admin")

        # Создание тестового пользователя
        self.admin_user = User.objects.create_user(username="admin", password="password123")
        self.admin_user.groups.add(self.admin_group)
        self.client.login(username="admin", password="password123")

        # Создание тестовых данных
        self.league = League.objects.create(
            name="Premier League",
            country="England",
            start_date="2024-01-01",
            end_date="2024-12-31",
        )
        self.club1 = Club.objects.create(name="Manchester United", value=100000000, country="GB")
        self.club2 = Club.objects.create(name="Liverpool", value=95000000, country="GB")

        self.standing1 = Standings.objects.create(league=self.league, club=self.club1, points=10)
        self.standing2 = Standings.objects.create(league=self.league, club=self.club2, points=8)

        self.match = Match.objects.create(
            league=self.league,
            home_team=self.club1,
            away_team=self.club2,
            home_team_score=2,
            away_team_score=1,
            match_date="2024-02-01",
        )

        # URL-ы для API
        self.league_url = reverse("league-list")
        self.match_url = reverse("match-list")
        self.standings_url = reverse("standing-list")

    def test_get_league_list(self):
        response = self.client.get(self.league_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_match_list(self):
        response = self.client.get(self.match_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_standings_list(self):
        response = self.client.get(self.standings_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_match_authorized(self):
        match_data = {
            "league": self.league.id,
            "home_team": self.club1.id,
            "away_team": self.club2.id,
            "home_team_score": 3,
            "away_team_score": 2,
            "match_date": "2024-03-01",
        }
        response = self.client.post(self.match_url, match_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_match_unauthorized(self):
        self.client.logout()
        match_data = {
            "league": self.league.id,
            "home_team": self.club1.id,
            "away_team": self.club2.id,
            "home_team_score": 3,
            "away_team_score": 2,
            "match_date": "2024-03-01",
        }
        response = self.client.post(self.match_url, match_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permissions_for_non_admin(self):
        non_admin_user = User.objects.create_user(username="user", password="password123")
        self.client.login(username="user", password="password123")

        match_data = {
            "league": self.league.id,
            "home_team": self.club1.id,
            "away_team": self.club2.id,
            "home_team_score": 3,
            "away_team_score": 2,
            "match_date": "2024-03-01",
        }
        response = self.client.post(self.match_url, match_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)