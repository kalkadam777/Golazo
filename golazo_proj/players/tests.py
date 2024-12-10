from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Player, Club

class PlayerAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.club = Club.objects.create(
            name="Manchester United",
            value=854000000,
            country="GB",
            league="Premier League"
        )
        cls.player1 = Player.objects.create(
            name="Harry Kane",
            position="Forward",
            value=100000000,
            country="FI",
            goals=5,
            assists=6,
            age=31,
            current_club=cls.club
        )
        cls.player2 = Player.objects.create(
            name="Harry Maguire",
            position="Defender",
            value=18000000,
            country="GB",
            goals=0,
            assists=0,
            age=31,
            current_club=cls.club
        )

    def test_list_players(self):
        url = reverse('player-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 2)  

    def test_search_players(self):
        url = reverse('player-list') + '?search=Harry'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2) 

    def test_filter_by_position(self):
        url = reverse('player-list') + '?position=Forward'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  

    def test_filter_by_value_range(self):
        url = reverse('player-list') + '?value__gte=50000000&value__lte=150000000'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1) 

    def test_ordering_players(self):
        url = reverse('player-list') + '?ordering=age'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], "Harry Kane")

    def test_create_player(self):
        url = reverse('player-create')
        data = {
            "name": "Marcus Rashford",
            "position": "Forward",
            "value": 75000000,
            "country": "GB",
            "goals": 15,
            "assists": 10,
            "age": 26,
            "current_club": self.club.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 3) 

    def test_pagination(self):
        url = reverse('player-list') + '?page=1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(response.data['current_page'], 1)  
        self.assertEqual(response.data['total_items'], 2) 