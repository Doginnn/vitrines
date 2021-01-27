from django.db import models


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Item(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.hotel_name