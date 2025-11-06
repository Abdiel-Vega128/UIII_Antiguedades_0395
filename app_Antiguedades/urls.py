# app_Antiguedades/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # General
    path('', views.inicio_antiguedades, name='inicio_antiguedades'),

    # CRUD Proveedores
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/actualizar/submit/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedores/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),

    # CRUD Piezas de Antigüedad
    path('piezas/', views.ver_piezas, name='ver_piezas'),
    path('piezas/agregar/', views.agregar_pieza, name='agregar_pieza'),
    path('piezas/actualizar/<int:pk>/', views.actualizar_pieza, name='actualizar_pieza'),
    path('piezas/actualizar/submit/<int:pk>/', views.realizar_actualizacion_pieza, name='realizar_actualizacion_pieza'),
    path('piezas/borrar/<int:pk>/', views.borrar_pieza, name='borrar_pieza'),
    
    # CRUD Clientes (NUEVOS) 👥
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/actualizar/submit/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),
]