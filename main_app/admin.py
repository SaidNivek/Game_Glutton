from django.contrib import admin
from .models import TrendingGame, Game

# Register your models here.
admin.site.register(TrendingGame)
admin.site.register(Game)