from django.shortcuts import render

from services.models import Service

# Create your views here.


def services_list(request):
    services = Service.objects.all().order_by("date")
    return render(request, "services.html", {"services": services})


def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    services = Service.objects.all().order_by("date")[:3]
    return render(request, "service_detail.html", {"service": service, "services": services})
