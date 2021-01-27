from django.db import models


#Classe que mostra a Vitrine(Pacote)
class Title(models.Model):
    title = models.CharField(max_length=100, verbose_name='Pacotes')
    subtitle = models.CharField(max_length=200, verbose_name='Descrição')


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name='Nome do Hotel')
    slug = models.CharField(max_length=100, verbose_name='Apelido do Hotel')
    image = models.URLField(verbose_name='Imagem')
    price = models.IntegerField(verbose_name='Valor R$')


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da cidade')
    slug = models.CharField(max_length=50, verbose_name='Apelido da cidade')
    state = models.CharField(max_length=50, verbose_name='Estado')
