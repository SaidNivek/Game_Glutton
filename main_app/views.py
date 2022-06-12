from multiprocessing import context
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from main_app.models import Game, TrendingGame, Wishlist, Collection, User
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trending_games"] = TrendingGame.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class GameDetail(DetailView):
    model = Game
    template_name = "game_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = Game.objects.all()
        return context   

class UserProfile(TemplateView):
    template_name = "user_profile.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wishlists"] = Wishlist.objects.filter(user_id=pk)
        print(context["wishlists"])
        context["collections"] = Collection.objects.filter(user_id=pk)
        return context   

class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = "user_update.html"
    succes_url = "/user/"

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.pk})

class SearchGame(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name") 

        if name != None:
            url = 'https://api.geekdo.com/xmlapi2/search?query=' + name
            req = requests.get(url)
            games = ET.fromstring(req.content)
            # Use the below code to remove any items that do not have a 'yearpublished' tag
            # if not removed, then there will be errors when adding to DB and when sorting by yearpublished
            if not games:
                context["header"] = f"Searching for {name}"
                context["footer"] = "No games found.  Try again?"
                return context
            for i in games.findall('item'):
                if i.find('yearpublished') == None:
                    games.remove(i)
            # Sort the remaining games by their year published date, which will be used to show the data in chronological order by release
            games[:] = sorted(games, key=lambda child: (child.tag,child.find('yearpublished').get('value')))
            # Only add the first 20 released games to the database and then show those as context
            for i in games.findall('item')[0:20]:
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
                    # Check to see if the game has an element of None
                    # If it does, give it a default error value to not break the system
                        my_image = the_game.find('image')
                        if my_image == None:
                            my_image = 'https://bitsofco.de/content/images/2018/12/broken-1.png'
                        else:
                            my_image = the_game.find('image').text
                        # Check to see if the game has an element of None
                        # If it does, give it a default error value to not break the system
                        my_thumbnail = the_game.find('thumbnail')
                        if my_thumbnail == None:
                            my_thumbnail = 'https://bitsofco.de/content/images/2018/12/broken-1.png'
                        else:
                            my_thumbnail = the_game.find('thumbnail').text
                        
                        game = Game(
                            bgg_id = bgg_id,
                            name = the_game.find('name').get('value'),
                            year_published = the_game.find('yearpublished').get('value'),
                            thumbnail = my_thumbnail,                            
                            img = my_image,
                            description = the_game.find('description').text.replace('&#10;', '\n'),
                            min_players = the_game.get('minplayers'),
                            max_players = the_game.get('maxplayers'),
                            min_playtime = the_game.get('minplaytime'),
                            max_playtime = the_game.get('maxplaytime'),
                            min_age = the_game.get('minage'),
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

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)