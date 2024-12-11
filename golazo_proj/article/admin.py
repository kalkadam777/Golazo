from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Article, Comment, assign_article_writer_role

admin.site.unregister(User)

@admin.action(description="Assign Article Writer Role")
def make_article_writer(modeladmin, request, queryset):
    for user in queryset:
        assign_article_writer_role(user)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    actions = [make_article_writer]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('title', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_at', 'content_short')
    ordering = ('-created_at',)
    search_fields = ('article__title', 'author__username', 'content')

    def content_short(self, obj):
        return (obj.content[:50] + '...') if len(obj.content) > 50 else obj.content
    content_short.short_description = 'Content (short)'