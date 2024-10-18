from django.contrib import admin
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'country')
    search_fields = ('name', 'country')
    list_filter = ('country',)

admin.site.register(Club, ClubAdmin)