import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from .models import Article
from .forms import ArticleForm
from .serializers import ArticleSerializer
from .permissions import IsArticleWriter
import os

# Создаем директорию для логов, если она не существует
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Настройка логгера для articles
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, 'articles.log'))
    ]
)
logger = logging.getLogger('articles')

@login_required
def create_article(request):
    if not request.user.groups.filter(name='Article Writer').exists():
        logger.warning(f"Permission denied for user '{request.user.username}' attempting to create an article.")
        raise PermissionDenied("You are not allowed to add articles.")

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            logger.info(f"Article '{article.title}' created by user '{request.user.username}'.")
            return redirect('article_list')
        else:
            logger.error(f"Form invalid for user '{request.user.username}' while creating an article.")
    else:
        form = ArticleForm()
    return render(request, 'article/create_article.html', {'form': form})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            logger.info(f"User '{self.request.user.username}' attempting to create an article.")
            return [permissions.IsAuthenticated(), IsArticleWriter()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        article = serializer.save(author=self.request.user)
        logger.info(f"API: Article '{article.title}' created by user '{self.request.user.username}'.")

def article_list(request):
    try:
        articles = Article.objects.all()
        logger.info("Article list accessed.")
        return render(request, 'article/article_list.html', {'articles': articles})
    except Exception as e:
        logger.error(f"Error accessing article list: {e}")
        raise
