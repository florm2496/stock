from django.shortcuts import render 
from .models import Cliente , FacturaDet ,FacturaEnc
from django.views import generic
from .forms import ClienteForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from datetime import datetime
from vino.views import VinoView
# Create your views here.
class ClienteView(generic.ListView):
    model = Cliente
    template_name = "ventas/clientes.html"
    context_object_name = "obj"
  

class VistaBaseCreate(SuccessMessageMixin , generic.CreateView):
    context_object_name='obj'
    success_message='registro agregado con exito'

    def form_valid(self , form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin , generic.UpdateView):
    context_object_name='obj'
    success_message='registro editado con exito'
    def form_valid(self , form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)


class ClienteNew(VistaBaseCreate):
    model=Cliente
    template_name="ventas/cliente_form.html"
    form_class=ClienteForm
    success_url= reverse_lazy("ventas:clientes")
    


class ClienteEdit(VistaBaseEdit):
    model=Cliente
    template_name="ventas/cliente_form.html"
    form_class=ClienteForm
    success_url= reverse_lazy("ventas:clientes")
  




class VentaListView(generic.ListView):
    model = FacturaEnc
    context_object_name='obj'
    template_name = "ventas/ventas.html"

#VISTA DE FUNCIONES

def Ventas(request , id=None):
    template_name='ventas/venta_form.html'
    encabezado={
        'fecha':datetime.today()
    }
    detalle={}
    clientes=Cliente.objects.filter(estado=True)
    context={'enc':encabezado,'det':detalle ,'clientes':clientes}

    return render(request , template_name, context)

class VinoView(VinoView):
    template_name='ventas/buscar_producto.html'
