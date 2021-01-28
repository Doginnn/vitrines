from django.db import models
# from vitrines.vitrines.models import Hotel, City, Country, Category


# Classe que mostra a Vitrine(Pacote)
class Evento(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tipo de pacote')
    subtitle = models.CharField(max_length=200, verbose_name='Descrição')


class Hotel(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True)
    hotel_name = models.CharField(max_length=100, verbose_name='Nome do Hotel')
    slug = models.SlugField(verbose_name='Apelido do hotel')
    image = models.URLField(verbose_name='Imagem')
    price = models.IntegerField(verbose_name='Valor R$')


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da cidade')
    slug = models.SlugField(verbose_name='Apelido da cidade')
    state = models.CharField(max_length=50, verbose_name='Abreviação do estado')


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do país')
    slug = models.SlugField(verbose_name='Apelido do país')
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da categoria')
    slug = models.SlugField(verbose_name='Apelido da categoria')

# hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
# city = models.ForeignKey(City, on_delete=models.CASCADE)
# country = models.ForeignKey(Country, on_delete=models.CASCADE)
# category = models.ForeignKey(Category, on_delete=models.CASCADE)
