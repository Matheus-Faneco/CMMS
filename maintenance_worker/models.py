from django.db import models

# Create your models here.

class MaintenanceWorker(models.Model):
    worker_name = models.CharField(
        max_length=16,
    )
    worker_role = models.CharField(
        max_length=50,
        default="Técnico"
    )
