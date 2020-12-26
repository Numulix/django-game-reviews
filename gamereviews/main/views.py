from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg

# Create your views here.
def home(request):
    allGames = Game.objects.all()
    return render(request, 'main/index.html', { 'games': allGames })

def detail(request, id):
    game = Game.objects.get(pk=id)
    reviews = Review.objects.filter(game=id)

    if reviews:
        average = reviews.aggregate(Avg('rating'))['rating__avg']
        average = round(average, 1)

        game.avg_rating = average
        game.save()

    return render(request, 'main/details.html', { 'game': game, 'reviews': reviews })


# Dodavanje igrice u bazu
def add_game(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                form = GameForm(request.POST or None)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('main:home')
            else:
                form = GameForm()
            return render(request, 'main/addgame.html', { 'form': form, 'controller': 'Add game' })
        else:
            return redirect('main:home')
    return redirect('accounts:login_user')


# Azuriranje postojece igrice u bazi
def edit_game(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            game = Game.objects.get(pk=id)

            if request.method == "POST":
                form = GameForm(request.POST or None, instance=game)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('main:detail', id)
            else:
                form = GameForm(instance=game)
            return render(request, 'main/addgame.html', {'form': form, 'controller': 'Edit game' })
        else:
            return redirect('main:home')
    return redirect('accounts:logins')

# Brisanje igrice iz baze
def delete_game(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            game = Game.objects.get(pk=id)

            game.delete()
            return redirect('main:home')
        else:
            return redirect('main:home')
    return redirect('accounts:logins')


def add_review(request, id):
    if request.user.is_authenticated:
        game = Game.objects.get(pk=id)

        if request.method == 'POST':
            form = ReviewForm(request.POST or None)

            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST['comment']
                data.rating = request.POST['rating']
                data.user = request.user
                data.game = game
                data.save()
                return redirect('main:detail', id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', { 'form': form })
    else:
        return redirect('accounts:login_user')


def edit_review(request, id_game, id_review):
    if request.user.is_authenticated:
        game = Game.objects.get(pk=id_game)
        review = Review.objects.get(game=game, id=id_review)

        if request.user == review.user:
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect('main:detail', id_game)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', { 'form': form })
        else:
            return redirect('main:details', id_game)
    else:
        return redirect('accounts:login_user')

def delete_review(request, id_game, id_review):
    if request.user.is_authenticated:
        game = Game.objects.get(id=id_game)
        review = Review.objects.get(game=game, id=id_review)

        if request.user == review.user:
            review.delete()
        return redirect('main:detail', id_game)
    else:
        return redirect('accounts:login_user')