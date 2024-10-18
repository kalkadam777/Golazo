from django.db import models
from django.contrib.auth.models import User
from players.models import Player
from clubs.models import Club

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_players = models.ManyToManyField(Player, blank=True, related_name='favorited_by')
    favorite_clubs = models.ManyToManyField(Club, blank=True, related_name='favorited_by')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'