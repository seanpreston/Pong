from django.db import models

from pong.profiles.models import UserProfile
from pong.util.models import PongModel


class Match(PongModel):

    name = models.CharField(max_length=255)

    player_one = models.ForeignKey(UserProfile, related_name='matches')
    player_two = models.ForeignKey(UserProfile, related_name='matches')

    @property
    def winner(self):
        games = self.games.all()
        player_one_wins = len([game.winner for game in games if game.winner == self.player_one])
        player_two_wins = len([game.winner for game in games if game.winner == self.player_two])

        if player_one_wins > player_two_wins:
            return self.player_one

        elif player_two_wins > player_one_wins:
            return self.player_two


class Game(PongModel):

    match = models.ForeignKey(Match, related_name='games')

    player_one = models.ForeignKey(UserProfile, related_name='games')
    player_one_score = models.IntegerField(default=0)

    player_two = models.ForeignKey(UserProfile, related_name='games')
    player_two_score = models.IntegerField(default=0)

    @property
    def winner(self):
        if self.player_one_score > self.player_two_score:
            return self.player_one

        elif self.player_two_score > self.player_one_score:
            return self.player_one
