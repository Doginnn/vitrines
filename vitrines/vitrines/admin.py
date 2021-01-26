from django.contrib import admin
from vitrines.vitrines.models import Hoteis

@admin.register(Hoteis)
class HoteisAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','subtitle',]
