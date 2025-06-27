from rest_framework.routers import DefaultRouter

from .viewset import MaintenanceWorkerViewset


router = DefaultRouter()
router.register(r'', MaintenanceWorkerViewset, basename='maintenance_worker')

urlpatterns = router.urls

