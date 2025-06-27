from rest_framework.routers import DefaultRouter

from .viewset import OrdersViewset

router = DefaultRouter()
router.register(r'', OrdersViewset, basename='orders')

urlpatterns = router.urls

