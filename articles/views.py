from django.shortcuts import render
from .models import Article
# Create your views here.


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/articles.html", {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    articles = Article.objects.all().order_by('date')[:3]
    return render(request, 'articles/article_detail.html', {'article': article, 'articles': articles})
