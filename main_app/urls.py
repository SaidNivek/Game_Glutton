from django.urls import path, include
from . import views
from django.contrib import admin

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('seed/', views.Seed.as_view(), name="seed"),
    path('search/game/', views.SearchGame.as_view(), name ="search_game"),
    path('games/<int:id>/', views.GameDetail.as_view(), name="game_detail"),
]