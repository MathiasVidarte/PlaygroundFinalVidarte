
from django.urls import path
from .import views
from .views import (
    HomePageView,
    CategoriasView,
    nosotros,
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
    path('nosotros/', nosotros, name='nosotros'),
    path('categorias/', CategoriasView.as_view(), name='categorias'),
    path('procesar-categoria/', procesar_categoria, name='procesar_categoria'),
    path('lista-categorias/', lista_categorias, name='lista_categorias'),
    path('producto/', producto, name='producto'),
    path('procesar-producto/', procesar_producto, name='procesar_producto'),
    path('cliente/', cliente, name='cliente'),
    path('buscar-clientes/', buscar_clientes, name='buscar_clientes'),
    path('procesar-cliente/', procesar_cliente, name='procesar_cliente'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile')
]
