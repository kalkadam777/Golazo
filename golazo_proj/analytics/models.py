from django.db import models
from players.models import Player

class PlayerStatistics(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='statistics')
    goals = models.IntegerField()
    assists = models.IntegerField()
    appearances = models.IntegerField()

    def __str__(self):
        return f"Statistics for {self.player.name}"

    class Meta:
        verbose_name = 'Player Statistics'
        verbose_name_plural = 'Player Statistics'