from django.shortcuts import render
from AppEntrega3 import models
from AppEntrega3 import forms
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    if request.method == "GET":
        return render(
            request,
            'AppEntrega3/inicio.html',
            {"form": forms.buscarCliente()}
        )
    else:
        email = request.POST['email']
        resultado = models.Clientes.objects.filter(email__icontains=email)
        textoResultado = f'El resultado de la busqueda para el cliente {email} es:'
        print(90*'-')
        print(resultado)
        print(type(resultado))
        for objeto in resultado:
             nombreCliente=(objeto.nombre)
             apellidoCliente=(objeto.apellido)
        textoNombre = f'Nombre Cliente: {nombreCliente}'
        textoApellido = f'Apellido Cliente: {apellidoCliente}'
        return render(request,
            'AppEntrega3/inicio.html',
            {"form": forms.buscarCliente(),'email':email, 'textoNombre':textoNombre,'textoApellido':textoApellido, 'textoResultado':textoResultado}
        )

def clientes(request):
    if request.method == "GET":
        return render(
            request,
            'AppEntrega3/clientes.html',
            {"form": forms.clientesFormulario()}
        )
    else:
        formulario = forms.clientesFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = models.Clientes(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            modelo.save()
        return render(
            request,
            'AppEntrega3/clientes.html',
            {"form": forms.clientesFormulario()}   
        )

def vendedores(request):
    if request.method == "GET":
        return render(
            request,
            'AppEntrega3/vendedores.html',
            {"form": forms.vendedoresFormulario()}
        )
    else:
        formulario = forms.vendedoresFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = models.Vendedores(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            modelo.save()
        return render(
            request,
            'AppEntrega3/vendedores.html',
            {"form": forms.vendedoresFormulario()}
        )
    # return render(request,'AppEntrega3/vendedores.html')

def productos(request):
    if request.method == "GET":
        return render(
            request,
            'AppEntrega3/productos.html',
            {"form": forms.productosFormulario()}
        )
    else:
        formulario = forms.productosFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = models.Productos(marca=informacion["marca"], modelo=informacion["modelo"],sku=informacion["sku"])
            modelo.save()
        return render(
            request,
            'AppEntrega3/productos.html',
            {"form": forms.productosFormulario()}
        )
    # return render(request,'AppEntrega3/productos.html')

def ventas(request):
    if request.method == "GET":
        return render(
            request,
            'AppEntrega3/ventas.html',
            {"form": forms.ventasFormulario()}
        )
    else:
        formulario = forms.ventasFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = models.Ventas(numeroVenta=informacion["numeroVenta"], fecha=informacion["fecha"],vendedor=informacion["vendedor"],cliente=informacion["cliente"])
            modelo.save()
        return render(
            request,
            'AppEntrega3/ventas.html',
            {"form": forms.ventasFormulario()}
        )
    # return render(request,'AppEntrega3/ventas.html')