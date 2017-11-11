from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from tictactoe.models import Game

@login_required
def home(request):
	my_game = Game.objects.games_for_user(request.user)
	active_game = my_game.filter(status= 'A')
	finished_game = my_game.exclude(status= 'A')
	waiting_game = active_game.filter(next_to_move=request.user)
	other_game = active_game.exclude(next_to_move=request.user)
	invitations = request.user.invitation_received.all()
	context = {'finished_game': finished_game,
				'waiting_game': waiting_game,
				'other_game': other_game,
				'invitations': invitations,
				}	
	print(context)
	return render(request, "user/home.html", context)

# Create your views here.
