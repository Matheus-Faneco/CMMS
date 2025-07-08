from django.db import models

# Create your models here.

class Machine(models.Model):

    MACHINE_STATUS = [
        ('O', 'Operational'),
        ('S', 'Stopped'),
        ('M', 'Maintenance')
    ]

    name = models.CharField(
        max_length=30
    )
    location = models.CharField(
        max_length=30
    )
    status = models.CharField(
        max_length=20,
        choices=MACHINE_STATUS,
        default="Operational"
    )



    def __str__(self):
        return f"{self.name} - {self.status}"