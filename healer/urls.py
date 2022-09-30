from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

# custom admin
admin.site.site_header = "Dr Irumba's Admin"
admin.site.site_title = "Dr Irumba's Admin"
admin.site.index_title = "Welcome to Dr Irumba's Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('', views.home),
    path('about/', views.about)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
