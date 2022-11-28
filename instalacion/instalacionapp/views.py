from re import template
from django.shortcuts import render, redirect
from .models import *
from .models import Post
from .models import Usuario
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden
from .models import tienda
# django nos permite tener forms#


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

    context = {'form': form}
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
def inicio(request):

    return render(request, 'social/inicio.html')

def filosofia(request):

    return render(request, 'social/filosofia.html')
def dudas(request):
    template = 'instalacionapp/dudas.html'
    if request.method == 'POST':

        dato = Dudas.objects.create(

            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            
        )
        dato.save()    
  
    return render(request, 'social/dudas.html')

def quejas(request):
    template = 'instalacionapp/quejas.html'
    if request.method == 'POST':

        dato = Quejas.objects.create(

            nombre2=request.POST['nombre2'],
            descripcion2=request.POST['descripcion2'],
            
        )
        dato.save()    
  
    return render(request, 'social/quejas.html')

def contrata(request):
    template = 'instalacionapp/contrata.html'
    if request.method == 'POST':

        dato = Contrata.objects.create(

            numero=request.POST['numero'],
            descripcion3=request.POST['descripcion3'],
            
        )
        dato.save()    
  
    return render(request, 'social/contrata.html')


def consulta(request):

    info = Post.objects.all()

    context = {'posts': info}

    return render(request, 'social/consul.html', context)






def consultati(request, username=None):
    ejemplo = tienda.objects.all()

    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'social/consultatienda.html', {'user': user, 'ejemplo': ejemplo})
