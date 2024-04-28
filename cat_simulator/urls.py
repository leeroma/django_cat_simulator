from django.urls import path

from cat_simulator.views import home_view, game_view, create_cat_view, set_state_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create_cat', create_cat_view, name='create_cat'),
    path('set_state', set_state_view, name='set_state'),
    path('game', game_view, name='game'),
]
