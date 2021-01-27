from django.db import models


#Classe que mostra a Vitrine(Pacote)
class Vitrine(models.Model):
    title = models.CharField(max_length=100, verbose_name='Pacotes')
    subtitle = models.CharField(max_length=200, verbose_name='Descrição')


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name='Nome do Hotel')
    slug = models.SlugField(verbose_name='Apelido do Hotel')
    image = models.URLField(verbose_name='Imagem')
    price = models.IntegerField(verbose_name='Valor R$')


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da cidade')
    slug = models.SlugField(verbose_name='Apelido da cidade')
    state = models.CharField(max_length=50, verbose_name='Abreviação do estado')


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do País')
    slug = models.SlugField(verbose_name='Apelido do país')


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do País')
    slug = models.SlugField(verbose_name='Apelido do país')
