from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Club


class ClubAPITestCase(APITestCase):

    def setUp(self):

        self.club = Club.objects.create(
            name="Test Club",
            value=1000000.00,
            country="US",
            league="Test League"
        )
        self.club_list_url = reverse('club-list')
        self.club_detail_url = reverse('club-detail', kwargs={'pk': self.club.id})
        self.club_create_url = reverse('club-create')
        self.club_update_url = reverse('club-update', kwargs={'pk': self.club.id})
        self.club_delete_url = reverse('club-delete', kwargs={'pk': self.club.id})

    def test_get_club_list(self):

        response = self.client.get(self.club_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Club", response.data[0]['name'])

    def test_get_club_detail(self):

        response = self.client.get(self.club_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Club")

    def test_create_club(self):

        data = {
            "name": "New Club",
            "value": "2000000.00",
            "country": "FR",
            "league": "New League"
        }
        response = self.client.post(self.club_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Club.objects.count(), 2)
        self.assertEqual(Club.objects.last().name, "New Club")

    def test_update_club(self):

        data = {
            "name": "Updated Club",
            "value": "3000000.00",
            "country": "GB",
            "league": "Updated League"
        }
        response = self.client.put(self.club_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.club.refresh_from_db()
        self.assertEqual(self.club.name, "Updated Club")
        self.assertEqual(self.club.league, "Updated League")

    def test_delete_club(self):

        response = self.client.delete(self.club_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Club.objects.count(), 0)
