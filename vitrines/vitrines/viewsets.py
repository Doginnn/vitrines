from rest_framework import viewsets
from vitrines.vitrines.models import Vitrine, Hotel
from vitrines.vitrines.serializers import VitrineSerializer, HotelSerializer

#Lista todas as vitrines
class VitrineViewSet(viewsets.ModelViewSet):
    queryset = Vitrine.objects.all()
    serializer_class = VitrineSerializer



#Criar a viewset para retornar a vitrine - CRUD;
#Criar a viewset para listar toda a vitrine - OK; ('')
#Criar a viewset para retornar a primeira e segunda vitrine criada "id 1 e id 2"; ('/')
#Criar a viewset para listar uma vitrine por ID; ('vitrines/destinos'); ('vitrines/destinos')
#Criar a viewset para retornar uma lista vazia; ('vitrines/sobre')
