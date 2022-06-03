from .models import *
import django_filters
# Para filtrar chazas --> pip install django-filter
class FiltroChazas(django_filters.FilterSet):
    class Meta:
        model = chaza
        fields = [
            'NombreChaza', 
            'Puntuacion',
            'Descripcion',
            'Ubicacion']