from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.prefetch_related('scopes__tag')
    context = {'object_list': object_list}    

    return render(request, template, context)
