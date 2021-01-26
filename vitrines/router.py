from vitrines.vitrines.viewsets import HoteisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hotel', HoteisViewSet)