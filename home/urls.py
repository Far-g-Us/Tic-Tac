from django.urls import path
from home.views import game_board, cell_clicked, game_view

urlpatterns = [
    path("game-board/", game_board, name="game_board"),
    path("cell_clicked/<int:row>/<int:col>/", cell_clicked, name="cell_clicked"),
    path('game/', game_view, name='game')
]
