from django.urls import path, include
from . import views
from django.contrib import admin

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('search/game/', views.SearchGame.as_view(), name ="search_game"),
    path('games/<slug:slug>/', views.GameDetail.as_view(), name="game_detail"),
    path('about/', views.About.as_view(), name="about"),
]