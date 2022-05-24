from django.db import models
from django.forms import ModelForm
from .models import comensales


class comensalesForm(ModelForm):
    class Meta:
        model = comensales
        fields = ['NombreUsuario', 'IdTipoUsuario']