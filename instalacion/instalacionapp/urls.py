from django.urls import path
from . import views

urlpatterns = [
    path('', views.miprimermetodo, name ="miprimermetodo"),
]