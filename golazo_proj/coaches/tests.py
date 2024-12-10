from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Manager, ManagingHistory
from clubs.models import Club


class ManagerAPITestCase(TestCase):
    def setUp(self):
        self.club1 = Club.objects.create(
            name="Real Madrid",
            country="ES",
            value=1000000000,
            league="La Liga"
        )
        self.club2 = Club.objects.create(
            name="Barcelona",
            country="ES",
            value=900000000,
            league="La Liga"
        )
        self.manager = Manager.objects.create(
            name="Pep Guardiola",
            current_club=self.club1,
            country="ES",
            age=50,
        )
        self.history = ManagingHistory.objects.create(
            manager=self.manager,
            club=self.club1,
            transfer_date="2022-01-01"
        )
        self.client = APIClient()
        self.list_url = reverse('manager-list')
        self.detail_url = reverse('manager-detail', kwargs={'pk': self.manager.pk})

    def test_get_manager_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.manager.name)

    def test_get_manager_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.manager.name)
        self.assertEqual(response.data['current_club'], self.club1.pk)

    def test_create_manager(self):
        data = {
            "name": "Xavi Hernandez",
            "current_club": self.club2.pk,
            "country": "ES",
            "age": 43,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Manager.objects.count(), 2)
        self.assertEqual(Manager.objects.last().name, "Xavi Hernandez")

    def test_update_manager(self):
        data = {
            "name": "Jose Mourinho",
            "current_club": self.club2.pk,
            "country": "PT",
            "age": 60,
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.manager.refresh_from_db()
        self.assertEqual(self.manager.name, "Jose Mourinho")

    def test_delete_manager(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Manager.objects.count(), 0)
