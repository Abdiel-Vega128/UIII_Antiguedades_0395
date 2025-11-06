# app_Antiguedades/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, PiezaAntiguedad, Cliente
from django.http import HttpResponse

# ==========================================
# GENERAL
# ==========================================
def inicio_antiguedades(request):
    """Página de inicio."""
    return render(request, 'inicio.html')

# ==========================================
# VISTAS CRUD PROVEEDOR (Existentes)
# ==========================================
def agregar_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            nombre_empresa=request.POST.get('nombre_empresa'),
            contacto=request.POST.get('contacto'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            especialidad=request.POST.get('especialidad'),
            años_experiencia=request.POST.get('años_experiencia')
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre_empresa = request.POST.get('nombre_empresa')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.email = request.POST.get('email')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.especialidad = request.POST.get('especialidad')
        proveedor.años_experiencia = request.POST.get('años_experiencia')
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', pk=pk) 

def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==========================================
# VISTAS CRUD PIEZA DE ANTIGÜEDAD (Existentes)
# ==========================================
def agregar_pieza(request):
    proveedores = Proveedor.objects.all() 
    if request.method == 'POST':
        proveedor_obj = get_object_or_404(Proveedor, pk=request.POST.get('proveedor'))
        PiezaAntiguedad.objects.create(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio=request.POST.get('precio'),
            año_fabricacion=request.POST.get('año_fabricacion'),
            estado_conservacion=request.POST.get('estado_conservacion'),
            proveedor=proveedor_obj,
            imagen=request.FILES.get('imagen')
        )
        return redirect('ver_piezas')
    return render(request, 'pieza/agregar_pieza.html', {'proveedores': proveedores})

def ver_piezas(request):
    piezas = PiezaAntiguedad.objects.all()
    return render(request, 'pieza/ver_piezas.html', {'piezas': piezas})

def actualizar_pieza(request, pk):
    pieza = get_object_or_404(PiezaAntiguedad, pk=pk)
    proveedores = Proveedor.objects.all()
    return render(request, 'pieza/actualizar_pieza.html', {'pieza': pieza, 'proveedores': proveedores})

def realizar_actualizacion_pieza(request, pk):
    pieza = get_object_or_404(PiezaAntiguedad, pk=pk)
    if request.method == 'POST':
        pieza.nombre = request.POST.get('nombre')
        pieza.descripcion = request.POST.get('descripcion')
        pieza.precio = request.POST.get('precio')
        pieza.año_fabricacion = request.POST.get('año_fabricacion')
        pieza.estado_conservacion = request.POST.get('estado_conservacion')
        proveedor_id = request.POST.get('proveedor')
        pieza.proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        if 'imagen' in request.FILES:
            pieza.imagen = request.FILES['imagen']
        pieza.save()
        return redirect('ver_piezas')
    return redirect('actualizar_pieza', pk=pk)

def borrar_pieza(request, pk):
    pieza = get_object_or_404(PiezaAntiguedad, pk=pk)
    if request.method == 'POST':
        pieza.delete()
        return redirect('ver_piezas')
    return render(request, 'pieza/borrar_pieza.html', {'pieza': pieza})

# ==========================================
# VISTAS CRUD CLIENTE (NUEVAS) 👥
# ==========================================

def agregar_cliente(request):
    """Muestra el formulario y maneja la adición de un nuevo cliente."""
    if request.method == 'POST':
        es_coleccionista = request.POST.get('es_coleccionista') == 'on' # Maneja el checkbox
        
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            estado_civil=request.POST.get('estado_civil'),
            es_coleccionista=es_coleccionista
        )
        return redirect('ver_clientes')
    
    # Proveedores solo se pasan si se maneja la relación M2M aquí, pero lo simplificaremos.
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    """Muestra la lista de todos los clientes."""
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, pk):
    """Muestra el formulario para actualizar un cliente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, pk):
    """Procesa la actualización de un cliente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        es_coleccionista = request.POST.get('es_coleccionista') == 'on' # Maneja el checkbox
        
        cliente.nombre = request.POST.get('nombre')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.estado_civil = request.POST.get('estado_civil')
        cliente.es_coleccionista = es_coleccionista
        
        cliente.save()
        return redirect('ver_clientes')
        
    return redirect('actualizar_cliente', pk=pk) 

def borrar_cliente(request, pk):
    """Muestra la confirmación para borrar un cliente."""
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})