from django.forms import ChoiceField
from .models import *
import django_filters
from django_filters import  *
from django.db.models import Q
# Para filtrar chazas --> pip install django-filter
class FiltroChazas(django_filters.FilterSet):
    #Puntuacion = ChoiceFilter(queryset=Puntuacion.objects.raw("SELECT Puntuacion from base_Puntuacion"))
    #Ubicacion = ChoiceFilter(queryset=Ubicacion.objects.raw("SELECT Ubicacion from base_Ubicacion"))
    my_lookup_field = django_filters.CharFilter(label='Chaza', method='my_lookup_method')
    
    def my_lookup_method(self, queryset, name, value):
        return queryset.filter((Q(NombreChaza__icontains=value)|Q(Descripcion__icontains=value)))
    class Meta:
        model = chaza
        fields = [
            'NombreChaza', 
            'Descripcion']
