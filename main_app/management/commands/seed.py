import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from ...models import TrendingGame

def get_trending_games():
    url = 'https://api.geekdo.com/xmlapi2/hot?boardgame'
    req = requests.get(url)
    games = ET.fromstring(req.content)
    return games

def seed_trending_games():
    games = get_trending_games()
    for i in games.findall('item'):
        game = TrendingGame(
            bgg_id = i.get('id'),
            name = i.find('name').get('value'),
            rank = i.get('rank'),
            thumbnail = i.find('thumbnail').get('value'),
            year_published = i.find('yearpublished').get('value')
        )
        game.save()

def clear_data():
  TrendingGame.objects.all().delete()

class Command(BaseCommand):
  def handle(self, *args, **options):
    clear_data()
    seed_trending_games()
    print("completed")