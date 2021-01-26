from django.db import models


class Hoteis(models.Model):
    title = models.Charfield(max_lenght=128)
    subtitle = models.Charfield(max_lenght=256)

    def __str__(self):
        return self.title
