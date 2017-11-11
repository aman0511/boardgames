from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
Game_Status_Choice = (
	('A', 'Active'),
	('B', 'first_player_win'),
	('C', 'second_player_win'),
	('D', 'Draw')
	)

FIRST_PLAYER_MOVE= 'X'
sECOND_PLAYER_MOVE= 'O'
BOARD_SIZE= 3

class GameManager(models.Manager):

	def as_board(self):
		board = [['' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
		for move in self.move_set.all():
			board[move.y][move.x] = FIRST_PLAYER_MOVE if move.by_first_player else SECOND_PLAYER_MOVE
		return board

	def games_for_user(self, user):
		return super(GameManager, self).get_queryset().filter(
			Q(first_player__id=user.id) | Q(second_player__id=user.id))
	def new_game(self, invitation):
		game = Game(first_player=invitation.to_user,
					second_player=invitation.from_user,
					next_to_move=invitation.to_user)
		return game

class Game(models.Model):
	first_player = models.ForeignKey(User, related_name = "games_first_player")
	second_player = models.ForeignKey(User, related_name = "games_second_player")
	next_to_move = models.ForeignKey(User, related_name = "games_to_move")
	start_time = models.DateTimeField(auto_now_add = True)
	last_active = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length=1, default='A', choices= Game_Status_Choice)

	objects = GameManager()

	def is_users_game(self, user):
		if self.first_player == user or self.second_player == user:
			pass


	def last_move(self):
		return self.move_set.latest()

	def is_users_move(self, user):
		return self.status == "A" and self.next_to_move == user 

	#def __str__(self):
		#return "{0} vs {1}".format(self.first_player, self.second_player)

	def get_absolute_url(self):
		return reverse ('tictactoe_game_detail', args=[self.id])

class Move(models.Model):
	x = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE-1)])
	y = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE-1)])
	by_first_player = models.BooleanField()
	timestamp = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=300)
	game = models.ForeignKey(Game)

class Meta:
	get_latest_by = 'timestamp'

	def player(self):
		return self.game.first_player if self.by_first_player else self.game.second_player

class Invitation(models.Model):
	from_user = models.ForeignKey(User, related_name = "invitation_sent")
	to_user = models.ForeignKey(User, related_name = "invitation_received", verbose_name="user to invite", 
		help_text="please select the user you want to play with")
	message = models.CharField("optional mesage", max_length = 100, blank = True, 
		help_text="Adding a friendly message is never a bad idea")
	time_stamp = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return "{0}- {1}".format(self.from_user, self.to_user)
