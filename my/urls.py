
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name="home"),
    path('skills/', views.skills , name="skills"),
    path('project/', views.project , name="project"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
