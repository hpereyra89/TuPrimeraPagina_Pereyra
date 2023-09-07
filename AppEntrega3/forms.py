from django import forms


class clientesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()

class vendedoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()

class productosFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    sku = forms.IntegerField()

class ventasFormulario(forms.Form):
    numeroVenta = forms.IntegerField(label="Numero de Venta")
    fecha = forms.DateField(input_formats="/%d/%m/%Y",label="Fecha (YYYY-MM-DD)")
    vendedor = forms.CharField()
    cliente = forms.CharField()

class buscarCliente(forms.Form):
    email = forms.CharField()