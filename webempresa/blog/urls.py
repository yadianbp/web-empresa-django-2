from django.urls import path
from . import views as views_blog

urlpatterns = [

    path('', views_blog.Blog, name='blog'),
    path('category/<int:category_id>/', views_blog.category, name='category')
]