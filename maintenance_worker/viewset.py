from rest_framework import viewsets
from .models import MaintenanceWorker
from .serializer import MaintenanceWorkerSerializer


class MaintenanceWorkerViewset(viewsets.ModelViewSet):
    queryset = MaintenanceWorker.objects.all()
    serializer_class = MaintenanceWorkerSerializer
