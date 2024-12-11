# /Users/lzandaribaev/Desktop/WEB/projects/Golazo/golazo_proj/article/views.py
import logging
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from .serializers import ArticleSerializer
from .permissions import IsArticleWriter

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[logging.FileHandler(os.path.join(LOG_DIR, 'articles.log'))]
)
logger = logging.getLogger('articles')

def home(request):
    latest_articles = Article.objects.order_by('-created_at')[:3]
    comment_form = CommentForm()
    return render(request, 'home.html', {
        'latest_articles': latest_articles,
        'comment_form': comment_form
    })

@login_required
def comment_create(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        article = get_object_or_404(Article, pk=article_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            logger.info(f"Comment created on article '{article.title}' by user '{request.user.username}'.")
        else:
            logger.error(f"Comment form invalid for user '{request.user.username}' on article '{article.title}'.")
        return redirect('home')
    else:
        return redirect('home')

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

def article_list(request):
    try:
        articles = Article.objects.all().order_by('-created_at')
        comment_form = CommentForm()  
        logger.info("Article list accessed.")
        return render(request, 'article/article_list.html', {
            'articles': articles,
            'comment_form': comment_form
        })
    except Exception as e:
        logger.error(f"Error accessing article list: {e}")
        raise

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            logger.info(f"User '{self.request.user.username}' attempting to create an article via API.")
            return [permissions.IsAuthenticated(), IsArticleWriter()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        article = serializer.save(author=self.request.user)
        logger.info(f"API: Article '{article.title}' created by user '{self.request.user.username}'.")