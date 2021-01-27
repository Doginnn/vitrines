from django.contrib import admin
from vitrines.vitrines.models import Vitrine, Hotel


admin.site.register(Vitrine, Hotel)
