from django.shortcuts import render
from .models import Cepa ,Vino ,Reserva,Bodega ,Unidad
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView ,TemplateView




class CepaView(LoginRequiredMixin,ListView):
    model=Cepa
    context_object_name='obj'
    template_name='vinos/cepas.html'
    login_url='bases:login'
class ReservaView(LoginRequiredMixin,ListView):
    model=Reserva
    context_object_name='obj'
    template_name='vinos/reservas.html'
    login_url='bases:login'
class BodegaView(LoginRequiredMixin,ListView):
    model=Bodega
    context_object_name='obj'
    template_name='vinos/bodegas.html'
    login_url='bases:login'
class UnidadView(LoginRequiredMixin,ListView):
    model=Unidad
    context_object_name='obj'
    template_name='vinos/unidades.html'
    login_url='bases:login'

class VinoView(LoginRequiredMixin,ListView): 
    model=Vino
    context_object_name='obj'
    template_name='vinos/vinos.html'
    login_url='bases:login'