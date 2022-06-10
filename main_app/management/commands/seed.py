import requests
import xml.etree.ElementTree as ET # Needed for XML parsing, to get the data we need into the DB
from django.core.management.base import BaseCommand
from ...models import TrendingGame, Game

# This function will make a GET request to the BGG API and return the 50 top trending agmes
def get_trending_games():
    url = 'https://api.geekdo.com/xmlapi2/hot?boardgame'
    req = requests.get(url)
    games = ET.fromstring(req.content)
    return games

# This function will take the GET request and save the items to the main_app_trendinggames DB
# The response from the BGG API is in XML format, so we must do some trickery to get the data to show properly
def seed_trending_games():
    games = get_trending_games()
    for i in games.findall('item'):
        game = TrendingGame(
            bgg_id = i.get('id'),
            name = i.find('name').get('value'),
            rank = i.get('rank'),
            thumbnail = i.find('thumbnail').get('value'),
            year_published = i.find('yearpublished').get('value'),
            slug = i.get('id')
        )
        game.save()

# This function will seed the master database with games from the trending games pull request, BUT ONLY IF they have not yet been added to the master games list. If they have been added, they will be skipped.
def seed_games():
    games = get_trending_games()
    for i in games.findall('item'):
        # Set the bgg_id to each individual games' BGG ID to check in our own DB
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

# This function will delete all of the games from the maon_app_trendinggames DB to ensure there are no duplicates when the database is seeded
def clear_trending_games_data():
  TrendingGame.objects.all().delete()
  # This is used to conditionally delete all the games from the database if needed during testing/implementation
  Game.objects.all().delete()

# This function extends the BaseCommand Class and allows for python3 manage.py seed to be run, which will delete the DB and then seed it with the top 50 top trending games
class Command(BaseCommand):
  def handle(self, *args, **options):
    clear_trending_games_data()
    seed_trending_games()
    seed_games()
    print("completed")