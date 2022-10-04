
from re import template
from django.shortcuts import render, redirect
from .models import *
from .models import Post
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#django nos permite tener forms#


# Create your views here.
# el context es para pedir datos a base 

def feed(request):
 
  return render(request, 'social/feed.html')


def perfil(request):
 
  return render(request, 'social/perfil.html')

 
def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/registro.html', context)



 


def login(request):
 
  return render(request, 'social/login.html')

@login_required
def retorno(request):
 
  return render(request, 'social/prueba.html')

def contacto(request):
  template = 'instalacionapp/contacto.html'
  if request.method == 'POST':  
       
        dato = Post.objects.create(
          
                user_id=request.POST['usuario'], 
                id_propiedad=request.POST['id_propiedad'], 
                tipo_propiedad=request.POST['tipo_propiedad'], 
                ubicacion=request.POST['ubicacion'], 
                metros_cuadrados=request.POST['metros_cuadrados'], 
                renta_o_venta=request.POST['renta_o_venta'], 
                precio=request.POST['precio'], 
                n_habitaciones=request.POST['n_habitaciones'],  
                estado_habitaciones=request.POST['estado_habitaciones'], 
                disponible=request.POST['disponible'], 

          )
        dato.save()
  return render(request, 'social/contacto.html')

     
    

