from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method== 'GET':
     return render(request, 'login.html')
    else:
       usuario = request.POST.get('usuario')
       senha = request.POST.get('senha')
       
       user = authenticate(username = usuario, password = senha)

       if user:
          login(request , user)

          return HttpResponse('autentificado')
       else:
          return HttpResponse('email ou senha invalidos')
       
def plataforma(request):
   if request.user.is_authenticated:
    return HttpResponse('plataforma')
   return HttpResponse('Voê precisa estar logado para vizualizar')
