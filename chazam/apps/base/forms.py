from django.db import models
from django.forms import ModelForm
import django_filters
from .models import *
from django.forms import ModelForm, TextInput,Textarea,Select
from .models import comensales, chaza
from django import forms
from django_starfield import Stars


class comensalesForm(ModelForm):
    class Meta:
        model = comensales
        fields = ['NombreUsuario', 'IdTipoUsuario']


class chazaForm(ModelForm):
    class Meta:
        model = chaza
 
        fields = ['NombreChaza', 'Descripcion', 'IdUbicacion','IdCategoria']
        widgets = {
            'NombreChaza': TextInput(attrs={
                'class': "form-control"
                }),
            'Descripcion': Textarea(attrs={
                'class': "form-control2"
                }),
            'IdUbicacion': Select(attrs={
                'class': "form-control1"
                })
        }
        
        

class resenasForm(ModelForm):
    class Meta:
        model = comentarios
        fields = ['DescripcionComentario', 'PuntuacionDada']
