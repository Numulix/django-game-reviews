from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    allGames = Game.objects.all()
    return render(request, 'main/index.html', { 'games': allGames })