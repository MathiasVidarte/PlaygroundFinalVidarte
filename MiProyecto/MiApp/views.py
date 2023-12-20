from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import CategoriaForm, ProductoForm, ClienteForm, CustomUserCreationForm, CustomUserUpdateForm
from .models import Cliente, Categoria, Producto


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
    return render(request, 'MiApp/categorias.html', {'form': form})

def procesar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría agregada correctamente.')
            return redirect('lista_categorias')  
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(request, 'MiApp/categorias.html', {'form': form, 'categorias': categorias})



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
    template_name = 'MiApp/categorias.html'

    def get(self, request, *args, **kwargs):
        form = CategoriaForm()
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

        return render(request, self.template_name, {'form': form, 'categorias': categorias})


def procesar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('producto')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = ProductoForm()
    
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'form': form, 'productos': productos})

def cliente_list(request):
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente agregado correctamente.')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
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
            # Puedes agregar un mensaje de éxito si lo deseas
            return redirect('cliente_list')
        else:
            # Puedes agregar un mensaje de error si lo deseas
            pass
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'MiApp/cliente.html', {'form': form, 'clientes': clientes})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})

def about_me(request):
    # Puedes agregar información sobre el creador y el proyecto aquí
    context = {
        'about_text': "¡Bienvenido a nuestro proyecto! Somos...",
    }
    return render(request, 'MiApp/blog/about.html', context)
