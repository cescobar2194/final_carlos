from django.db import models
from django.contrib import admin


class Plato(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()

    def _str_(self):
        return self.nombre

class Menu(models.Model):
    nombre= models.CharField(max_length=30)
    precio= models.IntegerField()
    platos= models.ManyToManyField(Plato, through='Menus')
    def _str_(self):
        return self.nombre

class Menus(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)


class MenusInLine(admin.TabularInline):
    model=Menus
    extra=1

class PlatoAdmin(admin.ModelAdmin):
    inlines=(MenusInLine,)
class MenuAdmin(admin.ModelAdmin):
    inlines=(MenusInLine,)
