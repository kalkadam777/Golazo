from rest_framework import serializers
from .models import Manager, ManagingHistory


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'# Include only essential fields
        
        
class ManagingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagingHistory
        fields = '__all__'