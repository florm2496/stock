from django.urls import path , include

from .views import ClienteView ,ClienteNew ,VinoView, ClienteEdit,VentaListView , Ventas
urlpatterns = [
    path('clientes/' , ClienteView.as_view() , name='clientes'),
    path('clientes/new/' , ClienteNew.as_view() , name='cliente_new'),
    path('clientes/clientedit/<int:pk>' , ClienteEdit.as_view() , name='cliente_edit'),
    path('ventas/' , VentaListView.as_view() , name='ventas'),
    path('ventas/ventanew/' ,Ventas , name='ventanew'),
    path('ventas/ventaedit/<int:id>' ,Ventas , name='ventaedit'),
    path('ventas/buscar/' ,VinoView.as_view() , name='buscar'),
]