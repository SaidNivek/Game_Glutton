from django.contrib import admin
from .models import TrendingGame, Game, Collection, Wishlist

# Register your models here.
admin.site.register(TrendingGame)
admin.site.register(Game)
admin.site.register(Collection)
admin.site.register(Wishlist)