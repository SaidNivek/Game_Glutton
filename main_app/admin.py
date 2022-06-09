from django.contrib import admin
from .models import TrendingGame, Game, Collection

# Register your models here.
admin.site.register(TrendingGame)
admin.site.register(Game)
admin.site.register(Collection)