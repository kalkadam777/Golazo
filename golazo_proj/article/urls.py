from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_article, article_list, ArticleViewSet, comment_create

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')

urlpatterns = [
    path('create/', create_article, name='create_article'),
    path('', article_list, name='article_list'),
    path('comment/create/', comment_create, name='comment_create'),
    path('api/', include(router.urls)),  
]