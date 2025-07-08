from rest_framework import viewsets
from .models import Orders
from .serializer import OrdersSerializer
from rest_framework.permissions import IsAuthenticated


class OrdersViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
