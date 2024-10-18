from django.contrib import admin
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'display_value_in_euros')
    search_fields = ('name', 'country')
    list_filter = ('country',)
    def display_value_in_euros(self, obj):
        return f"€{obj.value}"
    display_value_in_euros.short_description = 'Value (€)' 
admin.site.register(Club, ClubAdmin)