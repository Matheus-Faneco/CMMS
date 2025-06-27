from django.db import models

from machine.models import Machine


class Orders(models.Model):
    MAINTENANCE_TYPE = [
        ('P', 'Preventive'),
        ('C', 'Corrective')
    ]
    MAINTENANCE_ORDER_STATUS = [
        ('O', 'Open'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]

    fk_machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="maintenance_orders",
    )
    order_description = models.CharField(
        max_length=256
    )
    order_type = models.CharField(
        max_length=1,
        choices=MAINTENANCE_TYPE
    )
    order_status = models.CharField(
        max_length=1,
        choices=MAINTENANCE_ORDER_STATUS
    )

