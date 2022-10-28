from django.urls import path,re_path
from . import views
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.feed, name ="feed"),
    path('^perfil/$' , views.perfil, name="perfil"),
    path('^register/$' , views.registro, name="registro"),
    path('^login/$' , LoginView.as_view(template_name='social/login.html'), name="login"),
    path('^logout/$' , LogoutView.as_view(template_name='social/logout.html'), name="logout"),
    path('^contacto/$' , views.contacto, name="contacto"),
    path('^acceso/$' , views.retorno, name="prueba"),
    path('^carrusel/$' , views.carrusel, name="carrusel"),
    path('^consultas/$' , views.consulta, name="consul"),
    path('^correo/$' , views.correo, name="ema"),
    path('^tienda/$' , views.compras, name="tienda"),
    url('^consulta/$' , views.consultati, name="consultatienda"),
    path('consulta/<str:username>/' , views.consultati, name="consultatienda"),


]
