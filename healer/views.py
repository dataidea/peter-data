# from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
from services.models import Service


def home(request):
    # return HttpResponse("Home")
    articles = Article.objects.all().order_by("date")[:3]
    services = Service.objects.all().order_by("date")[:3]
    return render(request, "home.html", {"articles": articles, "services": services})


def about(request):
    # return HttpResponse("About")
    return render(request, "about.html")
