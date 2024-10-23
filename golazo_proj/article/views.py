from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

@login_required
def create_article(request):
    if request.user.groups.filter(name='Journalists').exists():
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                return redirect('article_detail', pk=article.pk)
        else:
            form = ArticleForm()

        return render(request, 'article/create_article.html', {'form': form})
    else:
        messages.error(request, "You are not a journalist and cannot create articles.")
        return redirect('home')

@login_required
def profile(request):
    is_journalist = request.user.groups.filter(name='Journalists').exists()
    
    context = {
        'is_journalist': is_journalist,
        'user': request.user,
    }
    return render(request, 'user_profiles/profile.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comment_set.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', pk=article.pk)

    return render(request, 'article/article_detail.html', {'article': article, 'comments': comments, 'form': form})