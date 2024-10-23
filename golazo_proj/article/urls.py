from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_article, name='create_article'),
    path('profile/', views.profile, name='profile'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
]