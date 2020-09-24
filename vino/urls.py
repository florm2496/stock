from django.urls import path , include 
from .views import CepaView , UnidadView , BodegaView , ReservaView , VinoView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('cepas/',CepaView.as_view(),name='cepas'),
    path('unidades/',UnidadView.as_view(),name='unidades'),
    path('reservas/',ReservaView.as_view(),name='reservas'),
    path('bodegas/',BodegaView.as_view(),name='bodegas'),
    path('vinos/',VinoView.as_view(),name='vinos'),
]