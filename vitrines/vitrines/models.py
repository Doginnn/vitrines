from django.db import models


# Classe que mostra a Vitrine(Pacote)
class Evento(models.Model):
    title = models.CharField(max_length=100, verbose_name='Evento')
    subtitle = models.CharField(max_length=200, verbose_name='Descrição')

    def __str__(self):
        return self.title


class Item(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100, verbose_name='Nome do Hotel')
    slug = models.SlugField(verbose_name='Apelido do hotel')
    image = models.URLField(verbose_name='Imagem')
    price = models.IntegerField(verbose_name='Valor R$')


# class Hotel(models.Model):
#     vitrine = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True)
#     hotel_name = models.CharField(max_length=100, verbose_name='Nome do Hotel')
#     slug = models.SlugField(verbose_name='Apelido do hotel')
#     image = models.URLField(verbose_name='Imagem')
#     price = models.IntegerField(verbose_name='Valor R$')


# class City(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Nome da cidade')
#     slug = models.SlugField(verbose_name='Apelido da cidade')
#     state = models.CharField(max_length=50, verbose_name='Abreviação do estado')


# class Country(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Nome do país')
#     slug = models.SlugField(verbose_name='Apelido do país')
#     city = models.ForeignKey(City, on_delete=models.CASCADE)


# class Category(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Nome da categoria')
#     slug = models.SlugField(verbose_name='Apelido da categoria')
