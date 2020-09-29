from django.shortcuts import render
from .models import Cepa ,Vino ,Reserva,Bodega ,Unidad
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView ,UpdateView, CreateView ,TemplateView
from .forms import CepaNewForm ,BodegaNewForm ,ReservaNewForm,UnidadNewForm,VinoNewForm
from django.urls import reverse_lazy


class CepaView(LoginRequiredMixin,ListView):
    model=Cepa
    context_object_name='obj'
    template_name='vinos/cepas.html'
    login_url='bases:login'

class CepaNew(LoginRequiredMixin, CreateView):
    model=Cepa
    form_class=CepaNewForm
    template_name='vinos/crearcepa.html'
    context_object_name='obj'
    success_url=reverse_lazy('vino:cepas')
    login_url='bases-login'
class CepaUpdate(LoginRequiredMixin, UpdateView):
    model=Cepa
    form_class=CepaNewForm
    template_name='vinos/crearcepa.html'
    context_object_name='obj'
    success_url=reverse_lazy('vino:cepas')
    login_url='bases-login'

class BodegaView(LoginRequiredMixin,ListView):
    model=Bodega
    context_object_name='obj'
    template_name='vinos/bodegas.html'
    login_url='bases:login'
class BodegaNew(LoginRequiredMixin , CreateView):
    model=Bodega
    form_class=BodegaNewForm
    context_object_name='obj'
    template_name='vinos/crearbodega.html'
    login_url='bases:login'
    success_url=reverse_lazy('vino:bodegas')
class BodegaUpdate(LoginRequiredMixin , UpdateView):
    model=Bodega
    form_class=BodegaNewForm
    context_object_name='obj'
    template_name='vinos/crearbodega.html'
    login_url='bases:login'
    success_url=reverse_lazy('vino:bodegas')   

class ReservaView(LoginRequiredMixin,ListView):
    model=Reserva
    context_object_name='obj'
    template_name='vinos/reservas.html'
    login_url='bases:login'

class ReservaNew(LoginRequiredMixin,CreateView):
    model=Reserva
    form_class=ReservaNewForm
    context_object_name='obj'
    template_name='vinos/crearreserva.html'
    success_url=reverse_lazy('vino:reservas')
    login_url='bases:login'
class ReservaUpdate(LoginRequiredMixin,UpdateView):
    model=Reserva
    form_class=ReservaNewForm
    context_object_name='obj'
    template_name='vinos/crearreserva.html'
    success_url=reverse_lazy('vino:reservas')
    login_url='bases:login'

class UnidadView(LoginRequiredMixin,ListView):
    model=Unidad
    context_object_name='obj'
    template_name='vinos/unidades.html'
    login_url='bases:login'
class UnidadNew(LoginRequiredMixin,CreateView):
    model=Unidad
    form_class=UnidadNewForm
    context_object_name='obj'
    template_name='vinos/crearunidad.html'
    success_url=reverse_lazy('vino:unidades')
    login_url='bases:login'
class UnidadUpdate(LoginRequiredMixin,UpdateView):
    model=Unidad
    form_class=UnidadNewForm
    context_object_name='obj'
    template_name='vinos/crearunidad.html'
    success_url=reverse_lazy('vino:unidades')
    login_url='bases:login'


class VinoView(LoginRequiredMixin,ListView): 
    model=Vino
    context_object_name='obj'
    template_name='vinos/vinos.html'
    login_url='bases:login'
class VinoNew(LoginRequiredMixin,CreateView): 
    model=Vino
    form_class=VinoNewForm
    context_object_name='obj'
    template_name='vinos/modalvino.html'
    success_url=reverse_lazy('vino:vinos')
    login_url='bases:login'
class VinoUpdate(LoginRequiredMixin,UpdateView): 
    model=Vino
    form_class=VinoNewForm
    context_object_name='obj'
    template_name='vinos/modalvino.html'
    success_url=reverse_lazy('vino:vinos')
    login_url='bases:login'