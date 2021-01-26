from django.contrib import admin
from vitrines.vitrines.models import Hotel

@admin.register(Hotel)
class HoteisAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','subtitle',]
