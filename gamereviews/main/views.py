from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allGames = Game.objects.all()
    return render(request, 'main/index.html', { 'games': allGames })

def detail(request, id):
    game = Game.objects.get(pk=id)
    return render(request, 'main/details.html', { 'game': game })


# Dodavanje igrice u bazu
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('main:home')
    else:
        form = GameForm()
    return render(request, 'main/addgame.html', { 'form': form })