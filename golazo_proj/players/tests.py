from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from clubs.models import Club
from .models import Player


class PlayerAPITestCase(APITestCase):
    def setUp(self):

        self.club = Club.objects.create(name="Test Club", value=5000000.00, country="US", league="Test League")


        self.player1 = Player.objects.create(
            name="Player 1",
            position="Forward",
            current_club=self.club,
            value=1000000.00,
            country="US",
            goals=10,
            assists=5,
            age=25
        )
        self.player2 = Player.objects.create(
            name="Player 2",
            position="Midfielder",
            current_club=self.club,
            value=2000000.00,
            country="GB",
            goals=20,
            assists=10,
            age=22
        )

        self.player_list_url = reverse('player-list')
        self.player_detail_url = reverse('player-detail', kwargs={'pk': self.player1.id})
        self.valuable_players_url = reverse('valuable-players-list')
        self.young_players_url = reverse('young-player-list')
        self.player_create_url = reverse('player-create')
        self.player_update_url = reverse('player-update', kwargs={'pk': self.player1.id})
        self.player_delete_url = reverse('player-delete', kwargs={'pk': self.player1.id})

    def test_player_list(self):

        response = self.client.get(self.player_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_player_detail(self):

        response = self.client.get(self.player_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.player1.name)

    def test_valuable_players(self):

        response = self.client.get(self.valuable_players_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Player 2")

    def test_young_players(self):

        response = self.client.get(self.young_players_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Player 2")

    def test_create_player(self):

        data = {
            "name": "Player 3",
            "position": "Defender",
            "current_club": self.club.id,
            "value": "1500000.00",
            "country": "FR",
            "goals": 5,
            "assists": 3,
            "age": 21
        }
        response = self.client.post(self.player_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 3)

    def test_update_player(self):

        data = {
            "name": "Updated Player 1",
            "position": "Goalkeeper",
            "current_club": self.club.id,
            "value": "1800000.00",
            "country": "ES",
            "goals": 12,
            "assists": 7,
            "age": 27
        }
        response = self.client.put(self.player_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.player1.refresh_from_db()
        self.assertEqual(self.player1.name, "Updated Player 1")
        self.assertEqual(self.player1.position, "Goalkeeper")

    def test_delete_player(self):

        response = self.client.delete(self.player_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Player.objects.count(), 1)
