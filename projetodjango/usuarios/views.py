from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method== 'GET':
     return render(request, 'login.html')
    else:
       username = request.POST.get('username')
       senha = request.POST.get('senha')
       
       user = authenticate(request, username = username, password = senha)

       if user is not None:
          login_django(request,user)
          

          return HttpResponse('autentificado')
       else:
          return HttpResponse('login ou senha invalidos')
       
@login_required(login_url="/auth/login/")
def plataforma(request):
   return HttpResponse('Voê precisa estar logado para vizualizar')
