from django.forms import ModelForm
from django import forms

from .models import Invitation, Move

class InvitationForm(ModelForm):
	class Meta:
		model = Invitation
		exclude = ['from_user']

class MoveForm(ModelForm):
	class Meta:
		model = Move
		exclude = ('game', 'by_first_player', 'comment')