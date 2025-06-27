from rest_framework.routers import DefaultRouter

from .viewset import MachineViewset


router = DefaultRouter()
router.register(r'', MachineViewset, basename='machine')

urlpatterns = router.urls

