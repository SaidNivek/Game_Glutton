from django.urls import path, include
from . import views
from django.contrib import admin

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('search/', views.SearchGame.as_view(), name ="search"),
    # The slug is the bgg_id, but passed into the slug field
    # This allows the trending games and specific games to have the same game_detail page, regardless of their ID number in the DB 
    path('games/<slug:slug>/', views.GameDetail.as_view(), name="game_detail"),
    path('about/', views.About.as_view(), name="about"),
]