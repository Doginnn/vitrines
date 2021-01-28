from rest_framework import viewsets
from vitrines.vitrines.models import Evento, Item, City
from vitrines.vitrines.serializers import EventoSerializer, ItemSerializer, CitySerializer


# Lista todas as vitrines
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(
            evento=self.kwargs['evento_pk']
        )


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

# Criar a viewset para retornar a vitrine - CRUD;
# Criar a viewset para listar toda a vitrine - OK; ('')
# Criar a viewset para retornar a primeira e segunda vitrine criada "id 1 e id 2"; ('/')
# Criar a viewset para listar uma vitrine por ID; ('vitrines/destinos'); ('vitrines/destinos')
# Criar a viewset para retornar uma lista vazia; ('vitrines/sobre')
