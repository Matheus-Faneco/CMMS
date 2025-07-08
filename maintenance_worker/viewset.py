from rest_framework import viewsets
from .models import MaintenanceWorker
from rest_framework.permissions import IsAuthenticated
from .serializer import MaintenanceWorkerSerializer


class MaintenanceWorkerViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MaintenanceWorker.objects.all()
    serializer_class = MaintenanceWorkerSerializer
