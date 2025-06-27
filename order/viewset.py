from rest_framework import viewsets
from .models import Orders
from .serializer import OrdersSerializer


class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
