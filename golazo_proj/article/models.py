from django.db import models
from django.contrib.auth.models import User, Group

def assign_article_writer_role(user):
    article_writer_group, created = Group.objects.get_or_create(name='Article Writer')
    user.groups.add(article_writer_group)
    user.save()

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

