from django.contrib import admin
from .models import LiveBroadcast

class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
    list_filter = ('name',)
    
admin.site.register(LiveBroadcast, BroadcastAdmin)
