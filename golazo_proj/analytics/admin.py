from django.contrib import admin
from .models import PlayerStatistics

class PlayerStatisticsAdmin(admin.ModelAdmin):
    list_display = ('player', 'goals', 'assists', 'appearances')
    search_fields = ('player__name',)

admin.site.register(PlayerStatistics, PlayerStatisticsAdmin)