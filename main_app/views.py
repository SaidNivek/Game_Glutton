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
            if len(name):
                url = 'https://api.geekdo.com/xmlapi2/search?query=' + name
                req = requests.get(url)
                games = ET.fromstring(req.content)
                # Use the below code to remove any items that do not have a 'yearpublished' tag
                # if not removed, then there will be errors when adding to DB and when sorting by yearpublished
                for i in games.findall('item'):
                    if i.find('yearpublished') == None:
                        games.remove(i)
                # Sort the remaining games by their year published date, which will be used to show the data in chronological order by release
                games[:] = sorted(games, key=lambda child: (child.tag,child.find('yearpublished').get('value')))
                # Only add the first 10 released games to the database and then show those as context
                for i in games.findall('item')[0:10]:
                    bgg_id = i.get('id') 
                    # Use the bgg_id to check to see if it exists in our static games database
                    checkID = Game.objects.filter(bgg_id__icontains=bgg_id)
                    # If the game does exist, do nothing, since we don't want duplicates of games, which would balloon our database
                    if checkID:
                        pass
                    # If the bgg_id is not in the main game database, do a get request for the sepcific game, using the game id as the parameter for the url search
                    # Add that game to the database
                    else:
                        url = 'https://api.geekdo.com/xmlapi2/thing?id=' + bgg_id
                        req = requests.get(url)
                        single_game = ET.fromstring(req.content)
                        for the_game in single_game.findall('item'):
                            game = Game(
                                bgg_id = bgg_id,
                                name = the_game.find('name').get('value'),
                                thumbnail = the_game.find('thumbnail').text,
                                year_published = the_game.find('yearpublished').get('value'),
                                img = the_game.find('image').text,
                                description = the_game.find('description').text.replace('&#10;', '\n'),
                                min_players = the_game.find('minplayers').get('value'),
                                max_players = the_game.find('maxplayers').get('value'),
                                min_playtime = the_game.find('minplaytime').get('value'),
                                max_playtime = the_game.find('maxplaytime').get('value'),
                                min_age = the_game.find('minage').get('value'),
                                slug = bgg_id
                            )
                            game.save()
                context["games"] = Game.objects.filter(name__icontains=name)
                context["header"] = f"Searching for {name}"
                context["footer"] = "If you did not find the game you expected, please try a more specific search."
            else:
                context["header"] = "Search for a game"
            return context
        else:
            context["header"] = "Search for a game"
        return context
