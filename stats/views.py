from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import GameRegisterForm
from .models import Game

def home(request):
    Games = Game.objects.all()

    context = {'Games': Games}

    return render(request, 'stats/home.html',context)

def about(request):
    return render(request, 'stats/about.html')

def newgame(request):
    if request.method == 'POST':
        form = GameRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your game has been created!')
            return redirect('stats-home')
    else:
        form = GameRegisterForm()
    return render(request, 'stats/newgame.html', {'form': form})

def game(request):
    return render(request, 'stats/game.html')