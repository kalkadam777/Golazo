from django.contrib import admin
from .models import Player, TransferHistory

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'current_club', 'value', 'age')
    search_fields = ('name', 'position')
    list_filter = ('current_club', 'position')

class TransferHistoryAdmin(admin.ModelAdmin):
    list_display = ('player', 'club', 'transfer_date', 'transfer_value')
    search_fields = ('player__name', 'club__name')
    list_filter = ('transfer_date',)

admin.site.register(Player, PlayerAdmin)
admin.site.register(TransferHistory, TransferHistoryAdmin)