from vitrines.vitrines.viewsets import HotelViewSet, ItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', HotelViewSet)
router.register('item', ItemViewSet)
