from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from django.views.generic.base import TemplateView
from main_app.models import Game
import requests




# Create views here.
class Home(TemplateView):
    template_name = "home.html"

class Seed(View):
    def get(self, request):
        return HttpResponse('Seed Database Home')

class GameDetail(View):
        def get(self, request):
            return HttpResponse('Seed Database Home')

class SearchGame(TemplateView):
    template_name = "search_game.html"

    def get_games(request):
        all_games = {}
        name = request.GET['name']
        url = 'https://api.geekdo.com/xmlapi2/search?query=' + name
        req = requests.get(url)
        games = ET.fromstring(req.content)

        for i in games.findall('item'):
            game = Game(
                bgg_id = i.get('id'),
                name = i.find('name').get('value'),
                rank = i.get('rank'),
                thumbnail = i.find('thumbnail').get('value'),
                year_published = i.find('yearpublished').get('value'),
                img = i.find('image'),
                description = i.find('description'),
            )
            game.save()