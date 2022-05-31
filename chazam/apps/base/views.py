from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import comensales
from .forms import comensalesForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'goToLogin.html')

def finalSignup(request):
    idActual = str(request.user.id)
    o = comensales.objects.raw("SELECT * from base_comensales where RegistroFinal = "+idActual)
    count = 0
    for obj in o:
        count += 1
    if count != 0:
        return render(request, 'mainPage.html')
    else:
        return redirect(form_comensales)

@login_required
def mainPage(request):
    return render(request, 'mainPage.html')

def form_comensales(request ):
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

@login_required()
def uploadChazaInfo(request):
    return render(request, 'uploadChazaInfo.html')