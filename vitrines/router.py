from vitrines.vitrines.viewsets import TitleViewSet, HotelViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', TitleViewSet)
router.register('/', HotelViewSet)
# router.register('item', ItemViewSet)
# router.register('', HotelViewSet)
# router.register('item', ItemViewSet)
