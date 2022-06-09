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
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name") 
        # if name != None:
        #     context["games"] = Game.objects.filter(name__icontains=name)
        #     context["header"] = f"Searching for {name}"
        # else:
        #     context["header"] = "Search for a game"
        # return context

        if name != None:
            if len(name) > 4:
                url = 'https://api.geekdo.com/xmlapi2/search?query=' + name
                req = requests.get(url)
                games = ET.fromstring(req.content)
                print(games)
                context["header"] = f"Searching for {name}"
            elif len(name) <= 4:
                print("did not hit get route")
                context["header"] = "Search with more than 4 letters"
            else:
                context["header"] = "Search for a game"
            return context
        else:
            context["header"] = "Search for a game"
        return context

                # for i in games.findall('name'):
                #     the_game = Game(
                #         bgg_id = i.get('id'),                  
                #         name = the_game.find('name').get('value'),
                #         thumbnail = the_game.find('thumbnail').text,
                #         year_published = the_game.find('yearpublished').get('value'),
                #         img = the_game.find('image').text,
                #         description = the_game.find('description').text.replace('&#10;', '\n'),
                #         min_players = the_game.find('minplayers').get('value'),
                #         max_players = the_game.find('maxplayers').get('value'),
                #         min_playtime = the_game.find('minplaytime').get('value'),
                #         max_playtime = the_game.find('maxplaytime').get('value'),
                #         min_age = the_game.find('minage').get('value'),
                #         slug = i.get('id')
                #     )
                    
                    # the_game.save()