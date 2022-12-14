from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.articles_list, name="list"),
    path('<str:slug>', views.article_detail, name="detail")
]
