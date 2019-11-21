from django.shortcuts import render
from django.contrib import messages
from .forms import MenuForm
from pelicula.models import Menu, Menus
# Create your views here.

def ListaMenus(request):
    menus = Menus.objects.all
    return render(request, 'menus/ListaMenu.html', {'menus':menus})

def menu_nuevo(request):
    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
            menu = Menu.objects.create(nombre=formulario.cleaned_data['nombre'], precio=formulario.cleaned_data['precio'])
            for plato_id in request.POST.getlist('platos'):
                menus = Menus(plato_id=plato_id, menu_id = menu.id)
                menus.save()
            messages.add_message(request, messages.SUCCESS, 'Menu Guardado Exitosamente')

    else:
        formulario = MenuForm()
    return render(request,'menus/menu_editar.html')
