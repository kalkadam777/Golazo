from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Article

class ArticleTests(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Article Writer')
        self.user = User.objects.create_user(username='writer', password='password123')
        self.user.groups.add(self.group)
        self.client = Client()
        self.client.login(username='writer', password='password123')
        self.non_writer = User.objects.create_user(username='non_writer', password='password456')

    def test_create_article_page_accessible_for_writer(self):
        response = self.client.get(reverse('create_article'))
        self.assertEqual(response.status_code, 200)

    def test_create_article_page_denied_for_non_writer(self):
        self.client.login(username='non_writer', password='password456')
        response = self.client.get(reverse('create_article'))
        self.assertEqual(response.status_code, 403)

    def test_create_article(self):
        data = {
            'title': 'Test Article',
            'content': 'This is a test article.',
        }
        response = self.client.post(reverse('create_article'), data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.first().title, 'Test Article')

class ArticleAPITests(APITestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Article Writer')
        self.user = User.objects.create_user(username='api_writer', password='password123')
        self.user.groups.add(self.group)
        self.client = APIClient()
        self.client.login(username='api_writer', password='password123')

        self.non_writer = User.objects.create_user(username='api_non_writer', password='password456')
        self.non_writer_client = APIClient()
        self.non_writer_client.login(username='api_non_writer', password='password456')

    def test_api_create_article_as_writer(self):
        data = {
            'title': 'API Test Article',
            'content': 'This is a test article via API.',
        }
        response = self.client.post('/articles/api/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.first().title, 'API Test Article')

    def test_api_create_article_denied_for_non_writer(self):
        data = {
            'title': 'Unauthorized Article',
            'content': 'This should not be created.',
        }
        response = self.non_writer_client.post('/articles/api/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Article.objects.count(), 0)