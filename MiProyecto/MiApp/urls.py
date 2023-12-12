
from django.urls import path
from .views import (
    HomePageView,
    categoria,
    procesar_categoria,
    lista_categorias,
    producto,
    procesar_producto,
    cliente,
    buscar_clientes,
    procesar_cliente,
)

urlpatterns = [
    path('index/', HomePageView.as_view(), name='home'),
    path('categoria/', categoria, name='categoria'),
    path('procesar-categoria/', procesar_categoria, name='procesar_categoria'),
    path('lista-categorias/', lista_categorias, name='lista_categorias'),
    path('producto/', producto, name='producto'),
    path('procesar-producto/', procesar_producto, name='procesar_producto'),
    path('cliente/', cliente, name='cliente'),
    path('buscar-clientes/', buscar_clientes, name='buscar_clientes'),
    path('procesar-cliente/', procesar_cliente, name='procesar_cliente'),
]
