from rest_framework import serializers
from .models import MaintenanceWorker

class MaintenanceWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceWorker
        fields = '__all__'