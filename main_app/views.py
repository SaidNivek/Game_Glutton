from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from main_app.models import Game, TrendingGame
import requests

# Create views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trending_games"] = TrendingGame.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class Seed(View):
    def get(self, request):
        return HttpResponse('Seed Database Home')

class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.all()
        return context   

class SearchGame(TemplateView):
    template_name = "search_game.html"

    def get_games(request):
        all_games = {}
        name = request.GET['name']
        url = 'https://api.geekdo.com/xmlapi2/search?query=' + name
        req = requests.get(url)
        games = ET.fromstring(req.content)

        for i in games.findall('item'):
            the_game = Game(
                bgg_id = i.get('id'),
                name = i.find('name').get('value'),
                rank = i.get('rank'),
                thumbnail = i.find('thumbnail').get('value'),
                year_published = i.find('yearpublished').get('value'),
                img = i.find('image'),
                description = i.find('description'),
                min_players = the_game.find('minplayers').get('value'),
                max_players = the_game.find('maxplayers').get('value'),
                playtime = the_game.find('playingtime').get('value'),
                min_age = the_game.find('minage').get('value')
            )
            the_game.save()