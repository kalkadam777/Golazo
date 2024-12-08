from django.test import TestCase
from django.urls import reverse
from clubs.models import Club
from django.core.files.uploadedfile import SimpleUploadedFile


class ClubTestCase(TestCase):
    def setUp(self):
        """Создаём тестовые данные"""
        self.club = Club.objects.create(
            name="Test Club",
            value=1000000.00,
            country="England",
            league="Premier League",
            emblem=SimpleUploadedFile("test_emblem.jpg", b"file_content", content_type="image/jpeg"),
        )

    def test_club_creation(self):
        """Тест создания клуба"""
        self.assertEqual(self.club.name, "Test Club")
        self.assertEqual(self.club.country, "England")
        self.assertEqual(self.club.league, "Premier League")

    def test_club_list_view(self):
        """Тест списка клубов"""
        response = self.client.get(reverse('club-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Club")
        self.assertTemplateUsed(response, 'clubs/club_list.html')

    def test_club_detail_view(self):
        """Тест детальной информации о клубе"""
        response = self.client.get(reverse('club-detail', args=[self.club.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Club")
        self.assertTemplateUsed(response, 'clubs/club_detail.html')

    def test_club_create_view(self):
        """Тест создания нового клуба через представление"""
        response = self.client.post(reverse('club-create'), {
            'name': 'New Club',
            'value': 2000000.00,
            'country': 'Spain',
            'league': 'La Liga',
            'emblem': SimpleUploadedFile("new_emblem.jpg", b"new_file_content", content_type="image/jpeg"),
        })
        self.assertEqual(response.status_code, 302)  # Успешный редирект после создания
        self.assertTrue(Club.objects.filter(name='New Club').exists())

    def test_club_update_view(self):
        """Тест обновления клуба через представление"""
        response = self.client.post(reverse('club-update', args=[self.club.pk]), {
            'name': 'Updated Club',
            'value': 1500000.00,
            'country': 'England',
            'league': 'Championship',
            'emblem': SimpleUploadedFile("updated_emblem.jpg", b"updated_file_content", content_type="image/jpeg"),
        })
        self.assertEqual(response.status_code, 302)  # Успешный редирект после обновления
        self.club.refresh_from_db()
        self.assertEqual(self.club.name, 'Updated Club')
        self.assertEqual(self.club.league, 'Championship')

    def test_club_delete_view(self):
        """Тест удаления клуба"""
        response = self.client.post(reverse('club-delete', args=[self.club.pk]))
        self.assertEqual(response.status_code, 302)  # Успешный редирект после удаления
        self.assertFalse(Club.objects.filter(pk=self.club.pk).exists())
