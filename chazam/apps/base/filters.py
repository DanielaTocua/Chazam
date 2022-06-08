from django import forms
from django.forms import ChoiceField
from .models import *
import django_filters
from django import forms
from django_filters import  *
from django.db.models import Q
# Para filtrar chazas --> pip install django-filter
class FiltroChazas(django_filters.FilterSet):
    class Meta:
        model = chaza
        fields = [
            'NombreChaza', 
            'Descripcion',
            'IdCategoria']

    CHOICES_CATEGORIAS = []
    CHOICES_UBICACIONES = []
    CHOICES_PUNTUACIONES = [(1,1),(2,2),(3,3),(4,4),(5,5)]
    # Obtengo todas las categorias y las ubicaciones y las meto a sus CHOICES
    categorias = categoria.objects.all()
    ubicaciones = Ubicaciones.objects.all()
    # print(categorias)
    
    
    i = 1
    for IdCategoria in categorias:
        CHOICES_CATEGORIAS.append((i,IdCategoria))
        # print(IdCategoria)
        i+=1
    i = 1
    for IdUbicacion in ubicaciones:
        CHOICES_UBICACIONES.append((i,IdUbicacion))
        # print(IdUbicacion)
        i+=1
    
    # Personalizo los filtros
    Categorias = django_filters.MultipleChoiceFilter(
        label='Categorias',
        choices = CHOICES_CATEGORIAS,
        widget = forms.CheckboxSelectMultiple(),
        method = 'Categorias_method'
        )

    Ubicaciones = django_filters.MultipleChoiceFilter(
        label='Ubicaciones',
        choices = CHOICES_UBICACIONES,
        widget = forms.CheckboxSelectMultiple(),
        method = 'Ubicaciones_method'
        )
    Puntuaciones = django_filters.MultipleChoiceFilter(
        label='Puntuaciones',
        choices = CHOICES_PUNTUACIONES,
        widget = forms.CheckboxSelectMultiple(),
        method = 'Puntuaciones_method'
        )
    
    my_lookup_field = django_filters.CharFilter(
        label='Chaza', 
        method='my_lookup_method'
    )
    
    # Métodos :3
    def Categorias_method(self, queryset, name, value):
        print("queryset",queryset)
        print("name",name)
        print("value",value)
        return queryset.filter((Q(IdCategoria__in=value)))    
    
    def Ubicaciones_method(self, queryset, name, value):
        print("queryset",queryset)
        print("name",name)
        print("value",value)
        return queryset.filter((Q(IdUbicacion__in=value)))    
    
    def Puntuaciones_method(self, queryset, name, value):
        print("queryset",queryset)
        print("name",name)
        print("value",value)
        return queryset.filter((Q(Puntuacion__in=value)))
        
    def my_lookup_method(self, queryset, name, value):
        return queryset.filter((Q(NombreChaza__icontains=value)|Q(Descripcion__icontains=value)))
    
    
    
