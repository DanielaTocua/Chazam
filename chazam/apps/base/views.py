from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    return render(request, 'goToLogin.html')

@login_required
def mainPage(request):
    return render(request, 'mainPage.html')