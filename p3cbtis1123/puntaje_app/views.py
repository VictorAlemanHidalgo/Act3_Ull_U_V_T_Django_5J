from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Administradores(request):
    return render(request, 'Administradores.html')

def Afiliados(request):
    return render(request, 'Afiliados.html')

def Servicios(request):
    return render(request, 'Servicios.html')

def Productos(request):
    return render(request, 'Productos.html')