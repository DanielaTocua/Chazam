from django.db import models
from django.forms import ModelForm
import django_filters
from .models import *


class comensalesForm(ModelForm):
    class Meta:
        model = comensales
        fields = ['NombreUsuario', 'IdTipoUsuario']


