from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    allGames = Game.objects.all()
    return render(request, 'main/index.html', { 'games': allGames })

def detail(request, id):
    game = Game.objects.get(pk=id)
    return render(request, 'main/details.html', { 'game': game })