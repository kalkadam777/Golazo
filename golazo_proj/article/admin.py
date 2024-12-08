from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Article, assign_article_writer_role

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