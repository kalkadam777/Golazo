from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'content')
    search_fields = ('article', 'author')
    list_filter = ('article', 'author')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)



