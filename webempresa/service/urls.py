from django.urls import path
from . import views as views_service

urlpatterns = [
   path('', views_service.Services, name='services'),
]
