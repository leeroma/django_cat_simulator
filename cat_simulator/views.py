from django.shortcuts import render, redirect

from cat_simulator.models import Cat


def home_view(request):
    return render(request, 'index.html')


def create_cat_view(request):
    Cat.objects.create(name=request.POST['name'])
    return redirect('game')


def set_state_view(request):
    cat = Cat.objects.first()
    action = request.POST['action'].lower()
    getattr(cat, action)()
    cat.save()
    return redirect('game')


def game_view(request):
    cat = Cat.objects.first()
    image = f'/{cat.state}.png'
    return render(request, 'game.html', {'image': image, 'cat': cat})
