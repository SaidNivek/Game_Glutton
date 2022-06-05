from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Game Glutton Home")

class Seed(View):
    def get(self, request):
        return HttpResponse('Seed Database Home')

class GameDetail(View):
        def get(self, request):
            return HttpResponse('Seed Database Home')