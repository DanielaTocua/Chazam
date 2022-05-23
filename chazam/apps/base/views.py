from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import comensales

# Create your views here.
def login(request):
    return render(request, 'goToLogin.html')

def finalSignup(request):
    idActual = str(request.user.IdComensal)
    o = comensales.objects.raw("SELECT * from base_comensales where RegistroFinalizado = "+idActual)
    count = 0
    for obj in o:
        count += 1
    if count != 0:
        return render(request, 'mainPage.html')
    else:
        return render(request, 'finalSignup.html')

@login_required
def mainPage(request):
    return render(request, 'mainPage.html')