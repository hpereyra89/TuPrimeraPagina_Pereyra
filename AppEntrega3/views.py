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
        modelo = models.Clientes(nombre=request.POST["nombre"], apellido=request.POST["apellido"],email=request.POST["email"])
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
        modelo = models.Vendedores(nombre=request.POST["nombre"], apellido=request.POST["apellido"],email=request.POST["email"])
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
        modelo = models.Productos(marca=request.POST["marca"], modelo=request.POST["modelo"],sku=request.POST["sku"])
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
        modelo = models.Ventas(numeroVenta=request.POST["numeroVenta"], fecha=request.POST["fecha"],vendedor=request.POST["vendedor"],cliente=request.POST["cliente"])
        modelo.save()
        return render(
            request,
            'AppEntrega3/ventas.html',
            {"form": forms.ventasFormulario()}
        )
    # return render(request,'AppEntrega3/ventas.html')