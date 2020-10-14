from django.shortcuts import render
from .models import Cepa ,Vino ,Reserva,Bodega ,Unidad
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin ,PermissionRequiredMixin
from django.views.generic import ListView ,UpdateView, CreateView ,TemplateView
from .forms import CepaNewForm ,BodegaNewForm ,ReservaNewForm,UnidadNewForm,VinoNewForm
from django.urls import reverse_lazy



class CepaView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model=Cepa
    context_object_name='obj'
    template_name='vinos/cepas.html'
    login_url='bases:login'
    permission_required='vino.view_cepa'
    
class CepaNew(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    model=Cepa
    form_class=CepaNewForm
    template_name='vinos/crearcepa.html'
    context_object_name='obj'
    success_url=reverse_lazy('vino:cepas')
    login_url='bases-login'
    permission_required='vino.add_cepa'
class CepaUpdate(PermissionRequiredMixin,LoginRequiredMixin, UpdateView):
    model=Cepa
    form_class=CepaNewForm
    template_name='vinos/crearcepa.html'
    context_object_name='obj'
    success_url=reverse_lazy('vino:cepas')
    login_url='bases-login'
    permission_required='vino.change_cepa'
    #permission_required='vino.delete_cepa'

class BodegaView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model=Bodega
    context_object_name='obj'
    template_name='vinos/bodegas.html'
    login_url='bases:login'
    permission_required='vino.view_bodega'
class BodegaNew(PermissionRequiredMixin,LoginRequiredMixin , CreateView):
    model=Bodega
    form_class=BodegaNewForm
    context_object_name='obj'
    template_name='vinos/crearbodega.html'
    login_url='bases:login'
    success_url=reverse_lazy('vino:bodegas')
    permission_required='vino.add_bodega'
class BodegaUpdate(PermissionRequiredMixin,LoginRequiredMixin , UpdateView):
    model=Bodega
    form_class=BodegaNewForm
    context_object_name='obj'
    template_name='vinos/crearbodega.html'
    login_url='bases:login'
    success_url=reverse_lazy('vino:bodegas')   
    permission_required='vino.change_bodega'
class ReservaView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model=Reserva
    context_object_name='obj'
    template_name='vinos/reservas.html'
    login_url='bases:login'
    permission_required='vino.view_reserva'
  


    
    
    

class ReservaNew(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model=Reserva
    form_class=ReservaNewForm
    context_object_name='obj'
    template_name='vinos/crearreserva.html'
    success_url=reverse_lazy('vino:reservas')
    login_url='bases:login'
    permission_required='vino.add_reserva'

class ReservaUpdate(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model=Reserva
    form_class=ReservaNewForm
    context_object_name='obj'
    template_name='vinos/crearreserva.html'
    success_url=reverse_lazy('vino:reservas')
    login_url='bases:login'
    permission_required='vino.change_reserva'
    #permission_required='vino.delete_reserva'

class UnidadView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model=Unidad
    context_object_name='obj'
    template_name='vinos/unidades.html'
    login_url='bases:login'
    permission_required='unidad.view_unidad'
class UnidadNew(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model=Unidad
    form_class=UnidadNewForm
    context_object_name='obj'
    template_name='vinos/crearunidad.html'
    success_url=reverse_lazy('vino:unidades')
    login_url='bases:login'
    permission_required='unidad.add_unidad'
class UnidadUpdate(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model=Unidad
    form_class=UnidadNewForm
    context_object_name='obj'
    template_name='vinos/crearunidad.html'
    success_url=reverse_lazy('vino:unidades')
    login_url='bases:login'
    permission_required='unidad.change_unidad'

    

class VinoView(PermissionRequiredMixin,LoginRequiredMixin,ListView): 
    model=Vino
    context_object_name='obj'
    template_name='vinos/vinos.html'
    login_url='bases:login'
    permission_required='vino.view_vino'
class VinoNew(PermissionRequiredMixin,LoginRequiredMixin,CreateView): 
    model=Vino
    form_class=VinoNewForm
    context_object_name='obj'
    template_name='vinos/modalvino.html'
    success_url=reverse_lazy('vino:vinos')
    login_url='bases:login'
    permission_required='vino.add_vino'

    def get_context_data(self , **kwargs):
        context=super(VinoNew , self).get_context_data(**kwargs)
        context['cepa']=Cepa.objects.filter(estado=True)
        context['bodega']=Bodega.objects.filter(estado=True)
        context['unidad']=Unidad.objects.filter(estado=True)
        context['reserva']=Reserva.objects.filter(estado=True)
        print(context)
        return context




class VinoUpdate(PermissionRequiredMixin,LoginRequiredMixin,UpdateView): 
    model=Vino
    form_class=VinoNewForm
    context_object_name='obj'
    template_name='vinos/modalvino.html'
    success_url=reverse_lazy('vino:vinos')
    login_url='bases:login'
    permission_required='vino.change_vino'
    #permission_required='vino.delete_vino'