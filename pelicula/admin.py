from django.contrib import admin
from pelicula.models import Plato, PlatoAdmin, Menu, MenuAdmin

# Register your models here.
admin.site.register(Plato,PlatoAdmin)
admin.site.register(Menu,MenuAdmin)
