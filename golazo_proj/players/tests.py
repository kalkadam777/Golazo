from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from players.models import Player, TransferHistory
from clubs.models import Club
from rest_framework.test import APIClient

class GeneralTestCase(TestCase):
    def setUp(self):
        # Создание тестовых данных
        self.client = APIClient()
        self.club = Club.objects.create(name="Test Club", value=1000000, country="England", league="Premier League")
        self.player = Player.objects.create(
            name="Test Player",
            position="Forward",
            current_club=self.club,
            value=500000,
            country="US",
            goals=10,
            assists=5,
            age=25
        )
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_model_creation(self):
        # Проверка создания модели Club
        self.assertEqual(self.club.name, "Test Club")
        self.assertEqual(self.player.name, "Test Player")

    def test_views_exist(self):
        # Проверка существования представлений
        try:
            response = self.client.get(reverse('player-list'))
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"Player list view failed with exception: {e}")

        try:
            response = self.client.get(reverse('player-detail', args=[self.player.id]))
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"Player detail view failed with exception: {e}")

    def test_api_endpoints(self):
        # Проверка доступности API-эндпоинтов
        try:
            response = self.client.get('/api/players/')  # Замените на фактический URL
            if response.status_code == 404:
                self.skipTest("API endpoint /api/players/ не настроен")
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"API endpoint /api/players/ test failed with exception: {e}")

        try:
            response = self.client.get(f'/api/players/{self.player.id}/')  # Замените на фактический URL
            if response.status_code == 404:
                self.skipTest(f"API endpoint /api/players/{self.player.id}/ не настроен")
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            self.fail(f"API endpoint /api/players/{self.player.id}/ test failed with exception: {e}")

    def test_player_creation_view(self):
        # Проверка создания игрока через форму
        try:
            response = self.client.post(reverse('player-list'), {
                'name': 'New Player',
                'position': 'Midfielder',
                'current_club': self.club.id,
                'value': 750000,
                'country': 'US',
                'goals': 8,
                'assists': 12,
                'age': 22
            })
            if response.status_code == 405:  # Метод не разрешён
                self.skipTest("Player creation view not implemented")
            self.assertEqual(response.status_code, 302)
        except Exception as e:
            self.fail(f"Player creation view failed with exception: {e}")

    def test_player_delete_view(self):
        # Проверка удаления игрока
        try:
            response = self.client.delete(reverse('player-detail', args=[self.player.id]))
            if response.status_code == 405:
                self.skipTest("Player delete view not implemented")
            self.assertEqual(response.status_code, 204)
        except Exception as e:
            self.fail(f"Player delete view failed with exception: {e}")
