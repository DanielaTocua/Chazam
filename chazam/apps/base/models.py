from turtle import pos
from django.db import models
from django.forms import IntegerField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
class chaza(models.Model):
    IdChaza = models.AutoField(primary_key=True)
    NombreChaza = models.CharField(max_length=40, blank=False, null=False,  verbose_name="Nombre Chaza")
    Puntuacion = models.FloatField(blank=False, null=False)
    Descripcion = models.TextField(blank=False, null=False,  verbose_name="Descripción",)
    Ubicacion = models.CharField(max_length=200, blank=False, null=False,  verbose_name="Ubicación",)
    slug= models.SlugField(max_length=255, unique=True, default="default")
    def __str__(self):
        return self.NombreChaza
    def save(self, *args, **kwargs):
        self.slug = slugify(self.NombreChaza)
        super(chaza, self).save(*args, **kwargs)

class tipoUsuario(models.Model):
    IdTipoUsuario = models.AutoField(primary_key=True, )
    NombreTipoUsuario = models.CharField(max_length=30, blank=False, null=False, )

    def __str__(self):
        return self.NombreTipoUsuario

class categoria(models.Model):
    IdCategoria = models.AutoField(primary_key=True)
    IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE)
    NombreCategoria = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.NombreCategoria


class comensales(models.Model):
    IdComensal = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, primary_key=True,unique=True)
    IdTipoUsuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE, verbose_name="Tipo de Usuario", default=1)
    NombreUsuario = models.CharField(max_length=20, blank=False, null=False, verbose_name= "Nombre a Mostrar", default= "Superusuario")
    RegistroFinal = models.IntegerField(default=0)
    def __str__(self):
        return self.NombreUsuario

class comentarios(models.Model):
    IdComentario = models.AutoField(primary_key=True)
    IdComensal = models.ForeignKey(comensales, on_delete=models.CASCADE)
    IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE, verbose_name="Nombre de la chaza")
    DescripcionComentario= models.TextField(max_length=400, blank=False, null=False, verbose_name="Escribe tu reseña")
    PuntuacionDada = models.FloatField(blank=False, default=0, verbose_name="Puntuación")
    def __str__(self):
        return self.IdComentario + "." + self.DescripcionComentario

class DuenoChaza(models.Model):
    IdDuenoChaza = models.AutoField(primary_key=True)
    IdComensal = models.ForeignKey(comensales, on_delete=models.CASCADE)
    IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE)
    def __str__(self):
        return self.IdDuenoChaza

# class Producto(models.Model):
#     IdProducto = models.AutoField(primary_key=True)
#     IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE)
#     NombreProducto = models.CharField(max_length=30, blank=False, null=False)
#     Precio = models.FloatField(blank=False, null=False)
#     Imagen = models.ImageField()





    



    
