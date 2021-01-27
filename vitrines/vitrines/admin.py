from django.contrib import admin
from vitrines.vitrines.models import Hotel, Item


admin.site.register(Hotel, Item)
