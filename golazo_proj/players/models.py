from django.db import models
from clubs.models import Club

class Player(models.Model):
    POSITION_CHOICES = [
        ('Forward', 'Forward'),
        ('Midfielder', 'Midfielder'),
        ('Defender', 'Defender'),
        ('Goalkeeper', 'Goalkeeper'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    current_club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name='players')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stats = models.JSONField()  # JSON для статистики игрока (голы, передачи и т.д.)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.position})"

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

class TransferHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='transfers')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='transfers')
    transfer_date = models.DateField()
    transfer_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transfer of {self.player.name} to {self.club.name} on {self.transfer_date}"

    class Meta:
        verbose_name = 'Transfer History'
        verbose_name_plural = 'Transfer Histories'