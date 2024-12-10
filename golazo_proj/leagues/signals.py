from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import League, Standings
from clubs.models import Club

@receiver(post_save, sender=League)
def create_standings_for_league(sender, instance, created, **kwargs):
    if created:
        for club in Club.objects.filter(league=instance.name):
            Standings.objects.create(league=instance, club=club)