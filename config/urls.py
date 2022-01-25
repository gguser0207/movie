"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ais import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('recommend_movie/start/', views.recommend_movie_start),  # 영화 추천 시스템
    path('recommend_movie/form1/', views.recommend_movie_form1),
    path('recommend_movie/form2/', views.recommend_movie_form2),
    path('recommend_movie/form3/', views.recommend_movie_form3),
    path('recommend_movie/form4/', views.recommend_movie_form4),
    path('recommend_movie/form5/', views.recommend_movie_form5),
    path('recommend_movie/end/', views.recommend_movie_end),
    path('recommend_movie/end_ajax/', views.recommend_movie_end_ajax),
]
