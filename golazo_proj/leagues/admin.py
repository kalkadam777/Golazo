from django.contrib import admin
from .models import League, Match, Standings


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'start_date', 'end_date', 'logo_preview')
    list_filter = ('country', 'start_date', 'end_date')
    search_fields = ('name', 'country')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" style="width: 50px; height: auto;" />'
        return "No logo"
    logo_preview.allow_tags = True
    logo_preview.short_description = "Logo Preview"


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('league', 'home_team', 'away_team', 'home_team_score', 'away_team_score', 'match_date')
    list_filter = ('league', 'match_date')
    search_fields = ('home_team__name', 'away_team__name', 'league__name')


@admin.register(Standings)
class StandingsAdmin(admin.ModelAdmin):
    list_display = ('league', 'club', 'matches_played', 'wins', 'draws', 'losses', 'points')
    list_filter = ('league',)
    search_fields = ('club__name', 'league__name')