from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_article, article_list, ArticleViewSet

router = DefaultRouter()
router.register(r'api', ArticleViewSet, basename='article')

urlpatterns = [
    path('create/', create_article, name='create_article'), 
    path('', article_list, name='article_list'),  
]

urlpatterns += router.urls