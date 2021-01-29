from django.db import models


# Classe que mostra a Vitrine(Pacote)
class Evento(models.Model):
    title = models.CharField(max_length=100, verbose_name='Evento')
    subtitle = models.CharField(max_length=200, verbose_name='Descrição')

    def __str__(self):
        return self.title


class Item(models.Model):
    hotel_name = models.CharField(max_length=100, verbose_name='Nome do Hotel')
    slug = models.SlugField(verbose_name='Slug do hotel')
    image = models.URLField(verbose_name='Imagem')
    price = models.IntegerField(verbose_name='Valor R$')
    evento = models.ForeignKey(Evento, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey("City", null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey("Country", null=True, blank=True, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da categoria')
    slug = models.SlugField(verbose_name='Slug da categoria')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da cidade')
    slug = models.SlugField(verbose_name='Slug da cidade')
    state = models.CharField(max_length=50, verbose_name='Abreviação do estado', help_text='Ex.: RN')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do país')
    slug = models.SlugField(verbose_name='Slug do país')

    def __str__(self):
        return self.name
