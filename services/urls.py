from django.urls import path
from . import views

app_name = "service"

urlpatterns = [
    path('', views.services_list, name="list"),
    path("<str:slug>", views.service_detail, name="detail")
]
