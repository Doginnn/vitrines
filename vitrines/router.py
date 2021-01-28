from django.urls import path, include
# from rest_framework import routers
from rest_framework_nested import routers
from vitrines.vitrines.viewsets import EventoViewSet, ItemViewSet


api_router = routers.DefaultRouter()
api_router.register(r'eventos', EventoViewSet)

eventos_router = routers.NestedDefaultRouter(api_router, r"eventos", lookup="evento")
eventos_router.register(r"items", ItemViewSet, basename="evento-items")


urlpatterns = [
    path('', include(api_router.urls)),
    path('', include(eventos_router.urls)),
]

# path('/', tem que me retornar o primeiro e segundo pacote criado "id 1 e id 2"),
# path('/destinos', tem que me retornar o primeiro pacote criado "id 1"),
# path('/sobre', tem que me retornar uma lista vazia "[]"),
