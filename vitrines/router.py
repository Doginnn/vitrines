from vitrines.vitrines.viewsets import VitrineViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('vitrines', VitrineViewSet)

# path('/', tem que me retornar o primeiro e segundo pacote criado "id 1 e id 2"),
# path('/destinos', tem que me retornar o primeiro pacote criado "id 1"),
# path('/sobre', tem que me retornar uma lista vazia "[]"),
