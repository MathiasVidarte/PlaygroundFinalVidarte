from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CategoriaForm, ProductoForm, ClienteForm, CustomUserCreationForm, CustomUserUpdateForm
from .models import Cliente, Categoria, Producto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'MiApp/blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def nosotros(request):
    return render(request, 'miapp/blog/nosotros.html')


def categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria')
    else:
        form = CategoriaForm()
    return render(request, 'categorias.html', {'form': form})

def procesar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'form': form, 'categorias': categorias})

def lista_categorias(request):
    categorias_list = Categoria.objects.all()
    elementos_por_pagina = 5
    paginator = Paginator(categorias_list, elementos_por_pagina)

    page = request.GET.get('page')
    try:
        categorias = paginator.page(page)
    except PageNotAnInteger:
        categorias = paginator.page(1)
    except EmptyPage:
        categorias = paginator.page(paginator.num_pages)

    return render(request, 'lista_categorias.html', {'categorias': categorias})


class CategoriasView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'miapp/categorias.html')

def producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, 'producto.html', {'form': form})

def procesar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    return render(request, 'producto.html', {'form': form, 'productos': productos})

def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'form': form, 'clientes': clientes})

def buscar_clientes(request):
    if 'q' in request.GET:
        query = request.GET['q']
        clientes = Cliente.objects.filter(nombre__icontains=query)
    else:
        clientes = Cliente.objects.all()
    
    return render(request, 'cliente_list.html', {'clientes': clientes})

def procesar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'MiApp/cliente.html', {'form': form, 'clientes': clientes})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

