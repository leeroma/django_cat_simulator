from django.shortcuts import render, redirect

from cat_simulator.models import Cat


def home_view(request):
    return render(request, 'index.html')


def create_cat_view(request):
    if request.POST['name']:
        Cat.objects.create(name=request.POST['name'])
    else:
        Cat.objects.create()
    return redirect('game')


def set_state_view(request):
    cat = Cat.objects.last()
    action = request.POST['action'].lower()
    getattr(cat, action)()
    cat.check_stats()
    cat.save()
    return redirect('game')


def game_view(request):
    cat = Cat.objects.last()
    image = f'/{cat.state}.png'
    return render(request, 'game.html', {'image': image, 'cat': cat})
