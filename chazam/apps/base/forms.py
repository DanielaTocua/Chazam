from django.db import models
from django.forms import ModelForm
<<<<<<< Updated upstream
import django_filters
from .models import *
from django.forms import ModelForm, TextInput,Textarea
from .models import comensales, chaza
=======
from .models import *
>>>>>>> Stashed changes


class comensalesForm(ModelForm):
    class Meta:
        model = comensales
        fields = ['NombreUsuario', 'IdTipoUsuario']

<<<<<<< Updated upstream

class chazaForm(ModelForm):
    class Meta:
        model = chaza
        fields = ['NombreChaza', 'Descripcion', 'Ubicacion']
        widgets = {
            'NombreChaza': TextInput(attrs={
                'class': "form-control"
                }),
            'Descripcion': Textarea(attrs={
                'class': "form-control2"
                }), 
            'Ubicacion': TextInput(attrs={
                'class': "form-control1"
                })
        }

class resenasForm(ModelForm):
    class Meta:
        model = comentarios
        fields = ['IdChaza',  'DescripcionComentario', 'PuntuacionDada']
        
=======
class resenasForm(ModelForm):
    class Meta:
        model = comentarios
        fields = ['DescripcionComentario', 'PuntuacionDada']
>>>>>>> Stashed changes
