from django.contrib.auth.models import Group

def article_writer_context(request):
    return {
        'is_article_writer': request.user.groups.filter(name='Article Writer').exists()
        if request.user.is_authenticated else False
    }