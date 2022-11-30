from django.urls import path,re_path
from . import views
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.feed, name ="feed"),
    re_path('^perfil/$' , views.perfil, name="perfil"),
    re_path('^register/$' , views.registro, name="registro"),
    re_path('^login/$' , LoginView.as_view(template_name='social/login.html'), name="login"),
    re_path('^logout/$' , LogoutView.as_view(template_name='social/logout.html'), name="logout"),
    re_path('^inicio/$' , views.inicio, name="inicio"),
    re_path('^filosofia/$' , views.filosofia, name="filosofia"),
    re_path('^dudas/$' , views.dudas, name="dudas"), 
    re_path('^quejas/$' , views.quejas, name="quejas"),
    re_path('^contrata/$' , views.contrata, name="contrata"),
    re_path('^directorio/$' , views.directorio, name="directorio"),
  


]
