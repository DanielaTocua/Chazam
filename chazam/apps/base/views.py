from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.views.generic.detail import DetailView

# Vistas
def login(request):
    return render(request, 'goToLogin.html')

def finalSignup(request):
    idActual = str(request.user.id)
    o = comensales.objects.raw("SELECT * from base_comensales where RegistroFinal = "+idActual)
    count = 0
    for obj in o:
        count += 1
    if count != 0:
        return redirect(mainPage)
    else:
        return redirect(form_comensales)

@login_required
def mainPage(request):
    #Mira si el usuario actual es dueño o comensal
    idActual = str(request.user.id)
    user_is_owner = False
    try:
        customer = comensales.objects.get(IdComensal_id = idActual)
        if customer.IdTipoUsuario_id == 2:
            user_is_owner = True
    except:
        pass
    return render(request, 'mainPage.html', {'user_is_owner': user_is_owner})

def form_comensales(request):
    if request.method == 'POST':
        obj = comensales(request.user.id)
        form = comensalesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            obj.RegistroFinal = obj.IdComensal_id
            obj.save()
            return redirect(mainPage)
        else:
            context = {'form': form }      
            return render(request, 'finalSignup.html', context)
    else:
         tempUsername = request.user.username
         form = comensalesForm(initial={'NombreUsuario': tempUsername, 'IdTipoUsuario':1})
         context = {'form': form}
         return render(request, 'finalSignup.html', context)

def form_chaza(request ):
    idActual = str(request.user.id)
    if request.method == 'POST':
        #Revisa si el dueño ya tiene una chaza creada
        o = comensales.objects.raw("SELECT * from base_duenochaza where IdComensal_id = "+idActual)
        count = 0
        for obj in o:
            count += 1
        #Si la chaza ya existe, se modifican sus valores
        if count != 0:
            obj0 = DuenoChaza.objects.get(IdComensal_id = idActual)
            obj = chaza.objects.get(IdChaza = obj0.IdChaza_id)
            form = chazaForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                obj.save()
                return redirect(mainPage)
        #Si la chaza no existe, se crea desde 0
        else:
            obj = chaza()
            obj.Puntuacion = 0
            obj2 = DuenoChaza()
            form = chazaForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                obj.save()
                obj2.IdChaza_id = obj.IdChaza
                obj2.IdComensal_id = request.user.id
                obj2.save()
                return redirect(mainPage)
    else:
        idActual = str(request.user.id)
        #Cuando se abre, trata de buscar los datos de la chaza
        user_has_chaza = False
        try:
            obj0 = DuenoChaza.objects.get(IdComensal_id = idActual)
            obj = chaza.objects.get(IdChaza = obj0.IdChaza_id)  
            tempName = obj.NombreChaza
            tempDescription = obj.Descripcion
            tempUbicacion = obj.Ubicacion
            form = chazaForm(initial={'NombreChaza': tempName, 'Descripcion': tempDescription, 'Ubicacion': tempUbicacion})
            user_has_chaza = True
        #Si no hay datos de la chaza, crea el form por defecto
        except:
            form = chazaForm()
        context = {'form': form, 'user_has_chaza': user_has_chaza}
        return render(request, 'uploadChazaInfo.html', context)

@login_required
def uploadChazaInfo(request):
    #Mira si el usuario actual es dueño o comensal
    idActual = str(request.user.id)
    user_is_owner = False
    customer = comensales.objects.get(IdComensal_id = idActual)
    if customer.IdTipoUsuario_id == 2:
        user_is_owner = True
    if user_is_owner:
        return redirect(form_chaza)
    #Si el usuario es comensal, no puede subir una chaza
    else:
        return redirect(mainPage)

@login_required
def eraseChaza(request):
    try:
        #Borra los registros de la chaza en la base de datos
        idActual = str(request.user.id)
        instance = DuenoChaza.objects.get(IdComensal_id=idActual)
        tempIdChaza = instance.IdChaza_id
        instance.delete()
        instance2 = chaza.objects.get(IdChaza = tempIdChaza)
        instance2.delete()
    except:
        pass
    return redirect(mainPage)

@login_required()
def filtroChazas(request):
    #Mira si el usuario actual es dueño o comensal
    idActual = str(request.user.id)
    user_is_owner = False
    try:
        customer = comensales.objects.get(IdComensal_id = idActual)
        if customer.IdTipoUsuario_id == 2:
            user_is_owner = True
    except:
        pass
    chazas = chaza.objects.all()
    filtro = FiltroChazas(request.GET, queryset=chazas)
    chazas = filtro.qs
    context = {"filtro": filtro, "chazas":chazas, 'user_is_owner': user_is_owner}
    return render(request,"catalogo.html",context)


@method_decorator(login_required, name='dispatch')
class chaza_view(DetailView):
    template_name = 'chazaCustom.html'
    model = chaza