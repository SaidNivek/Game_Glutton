from django.urls import path, include
from . import views
from django.contrib import admin

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('seed/', views.Seed.as_view(), name="seed"),
    path('games/<int:id>/', views.GameDetail.as_view(), name="game_detail"),
]