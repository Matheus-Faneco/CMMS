from rest_framework import viewsets
from .models import Machine
from rest_framework.permissions import IsAuthenticated
from .serializer import MachineSerializer


class MachineViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
