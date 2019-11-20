from django import forms
from .models import Menu, Plato


class MenuForm(forms.ModelForm):
    class Meta:
        model= Menu
        fields =('nombre','precio','platos')

def _init_(self, *args, **kwargs):
    super(MenuForm, self).__init__(*args, **kwargs)
    self.fields["platos"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["platos"].help_text = "Ingrese los Platos para el Menu"
    self.fields["platos"].queryset = Actor.objects.all()
