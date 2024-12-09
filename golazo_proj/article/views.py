from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from .models import Article
from .forms import ArticleForm
from .serializers import ArticleSerializer
from .permissions import IsArticleWriter

@login_required
def create_article(request):
    if not request.user.groups.filter(name='Article Writer').exists():
        raise PermissionDenied("You are not allowed to add articles.")

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')  
    else:
        form = ArticleForm()
    return render(request, 'article/create_article.html', {'form': form})

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsArticleWriter()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/article_list.html', {'articles': articles})
