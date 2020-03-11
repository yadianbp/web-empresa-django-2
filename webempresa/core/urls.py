from django.urls import path
from . import views as views_core

urlpatterns = [

    path('', views_core.Home, name='home'),
    path('about/', views_core.About, name='about'),
    path('store/', views_core.Store, name='store'),
]