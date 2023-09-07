from django.contrib import admin
from django.urls import path
from AppEntrega3 import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('clientes/',views.clientes),
    path('vendedores/', views.vendedores),
    path('productos/', views.productos),
    path('ventas/', views.ventas),
]