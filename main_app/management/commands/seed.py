import requests
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from ...models import Game

def get_hot_games():
    url = 'https://api.geekdo.com/xmlapi2/hot?boardgame'
    req = requests.get(url)
    games = ET.fromstring(req.content)
    # parsed_games = ET.fromstring(games)
    # print(parsed_games)
    # return games

def seed_games():
    games =  get_hot_games()
    # for i in games:
    #     # print(i["name.value"])
    #     game = Game(
    #         name = i["name"]
    #     )
    #     game.save()

class Command(BaseCommand):
  def handle(self, *args, **options):
    seed_games()
    # clear_data()
    print("completed")