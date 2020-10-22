from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum ,Q
from ventas.models import FacturaEnc , FacturaDet ,Cliente
from vino.models import Vino
from django.contrib.auth.models import User
# Create your views here.

class Home( LoginRequiredMixin,generic.TemplateView):
    template_name='bases/home.html'
    login_url='bases:login'


def Dashboard(request):
    template_name='bases/dashboard.html'
    context={}
    
    prods=Vino.objects.all().count()
    ultimos_prod=Vino.objects.all().order_by('-fc')[:3]
    facs=FacturaEnc.objects.aggregate(Sum('total'))
    total_ventas=facs['total__sum']
    ventas_registradas=FacturaEnc.objects.count()
    users=User.objects.all()
    client=Cliente.objects.all().count()
    
    mv=FacturaDet.objects.values('vino__nombre').annotate(Sum('cantidad'))
    sinstock=Vino.objects.filter(existencia=0)

   
    valores=[]
    for objeto in Vino.objects.all():
        sm=objeto.sm
        if sm != None:
            if objeto.existencia < objeto.sm and objeto.existencia>0:
                queryset=Vino.objects.filter(Q(existencia__lt = sm ) & Q(existencia__gt = 0 ) )
                valores.append(queryset)

    #def UltimosMovimientos():
    ultimas_mod=Vino.objects.all().order_by('-fm')[:5]
    print(ultimas_mod)

    
    context={
        'prods':prods,
        'facs':total_ventas,
        'users':users,
        'client':client,
        'up':ultimos_prod,
        'mv':mv,
        'ss':sinstock,
        'sm':valores[0],
        'um':ultimas_mod,
        'vr':ventas_registradas,
    }

    return render(request, template_name, context)
