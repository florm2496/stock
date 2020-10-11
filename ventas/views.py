from django.shortcuts import render ,redirect
from .models import Cliente , FacturaDet ,FacturaEnc
from django.views import generic
from .forms import ClienteForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin ,PermissionRequiredMixin
from django.http import HttpResponse
from datetime import datetime
from vino.views import VinoView
from django.contrib import messages
from vino.models import Vino
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
class ClienteView(PermissionRequiredMixin,generic.ListView):
    model = Cliente
    template_name = "ventas/clientes.html"
    context_object_name = "obj"
    permission_required='ventas.view_cliente'
  

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
    permission_required='ventas.add_cliente'
    


class ClienteEdit(VistaBaseEdit):
    model=Cliente
    template_name="ventas/cliente_form.html"
    form_class=ClienteForm
    success_url= reverse_lazy("ventas:clientes")
    permission_required='ventas.update_cliente'
  




class VentaListView(generic.ListView):
    model = FacturaEnc
    context_object_name='obj'
    template_name = "ventas/ventas.html"
    permission_required='ventas.view_cliente'

#VISTA DE FUNCIONES
@login_required(login_url="/login/")
@permission_required("ventas.view_Encabezado_Factura",login_url="/login/")

def Ventas(request , id=None):
    template_name='ventas/venta_form.html'
    encabezado={
        'fecha':datetime.today()
    }
    detalle={}
    clientes=Cliente.objects.filter(estado=True)


    if request.method=='GET':
        enc=FacturaEnc.objects.filter(pk=id).first()
        if not enc:
            encabezado={
                'id':0,
                'fecha':datetime.today(),
                'cliente':0,
                'sub_total':0.00 ,
                'descuento':0.00 ,
                'total': 0.00
        
            }
            detalle=None
        else:
            encabezado={
                'id':enc.id,
                'fecha':enc.fecha,
                'cliente':enc.cliente,
                'sub_total':enc.sub_total,
                'descuento':enc.descuento,
                'total':enc.total


            }
          



        detalle=FacturaDet.objects.filter(factura=enc)
        contexto = {"enc":encabezado,"det":detalle,"clientes":clientes}
        return render(request,template_name,contexto)

    if request.method=='POST':
        cliente=request.POST.get("enc_cliente")
      
        fecha=request.POST.get("enc_fecha")
        cli=Cliente.objects.get(pk=cliente)
      

        if not id:
            enc=FacturaEnc(
                cliente=cli,
                fecha=fecha,
                uc=request.user

            )
            if enc:
                enc.save()
                id=enc.id
        else:
            enc=FacturaEnc.objects.filter(pk=id).first()
            if enc:
                enc.cliente=cli
                enc.save()
        if not id:
            messages.error(request , "No se puede continuar ,Numero de factura no detectado")
            return redirect("ventas:ventas")

        codigo=request.POST.get("codigo")
        cantidad=request.POST.get("cantidad")
        precio=request.POST.get("precio")
        s_total=request.POST.get("sub_total_detalle")
        descuento=request.POST.get("descuento_detalle")
        total=request.POST.get("total")

        prod=Vino.objects.get(codigo=codigo)


        det=FacturaDet(
            factura=enc,
            vino=prod,
            cantidad=cantidad,
            precio=precio,
            sub_total=s_total,
            descuento=descuento,
            total=total,
            uc=request.user
            )
        if det:
            det.save()
        return redirect('ventas:ventaedit',id=id)



    return render(request , template_name, contexto)

class VinoView(VinoView):
    template_name='ventas/buscar_producto.html'


'''
   ex=int(prod.existencia) 
        cant=int(cantidad)
        if ex <= cant:
            print('no hay suficiente stock' ,ex , cant)
           
            return HttpResponse(request ,'error')'''