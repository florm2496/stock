from django.urls import path , include

from .views import ComprasView, compras ,CompraDetDelete

urlpatterns=[
    path('compras/',ComprasView.as_view(), name="listacompras"),
    path('compras/new',compras, name="compras_new"),
    path('compras/edit/<int:compra_id>',compras, name="editarcompra"),
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="delete_detcompra"),
    
]