from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm
from models import Cliente

def categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria')
    else:
        form = CategoriaForm()
    return render(request, 'categoria.html', {'form': form})

def producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, 'producto.html', {'form': form})

def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = ClienteForm()
    return render(request, 'cliente.html', {'form': form})

def buscar_clientes(request):
    if 'q' in request.GET:
        query = request.GET['q']
        clientes = Cliente.objects.filter(nombre__icontains=query)
    else:
        clientes = Cliente.objects.all()
    
    return render(request, 'cliente_list.html', {'clientes': clientes})

