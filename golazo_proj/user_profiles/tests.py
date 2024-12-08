from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):
    def test_register_success(self):
        """Проверка успешной регистрации пользователя"""
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'password_confirm': 'securepassword123',
        })
        self.assertEqual(response.status_code, 302)  # Редирект на страницу логина
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_password_mismatch(self):
        """Проверка обработки ошибки при несовпадении паролей"""
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
            'password_confirm': 'differentpassword123',
        })
        self.assertEqual(response.status_code, 200)  # Форма перезагружается с ошибкой
        self.assertContains(response, "Passwords do not match.")
        self.assertFalse(User.objects.filter(username='testuser').exists())
