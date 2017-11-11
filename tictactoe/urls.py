from django.conf.urls import *

from tictactoe.views import new_invitation, accept_invitation, game_detail, game_do_move


urlpatterns = [
				url(r"^invites/$", new_invitation, name='tictactoe_invite' ),
				url(r'^invitation/(?P<pk>\d+)$', accept_invitation, name='tictactoe_invitation' ),
				url(r'^game/(?P<pk>\d+)$', game_detail, name='tictactoe_game_detail'),
				url(r'^game/(?P<pk>\d+)/do_move$', game_do_move, name='tictactoe_game_do_move'),
			]