from django.contrib import admin
from .models import Manager, ManagingHistory

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_club', 'country', 'age', 'photo')
    search_fields = ('name', 'current_club')
    list_filter = ('current_club', 'name',)
    
    
class ManagingHistoryAdmin(admin.ModelAdmin):
    list_display = ('manager', 'club', 'transfer_date')
    search_fields = ('name', 'club')
    list_filter = ('club',)
    

admin.site.register(Manager, ManagerAdmin)
admin.site.register(ManagingHistory, ManagingHistoryAdmin)
