from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('index/', views.HomePageView.as_view(), name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('categorias/', views.CategoriasView.as_view(), name='categorias'),
    path('procesar-categoria/', views.procesar_categoria, name='procesar_categoria'),
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('procesar-producto/', views.procesar_producto, name='procesar_producto'),
    path('procesar-cliente/', views.procesar_cliente, name='procesar_cliente'),
    path('cliente/', views.cliente_list, name='cliente_list'),
    path('buscar-clientes/', views.buscar_clientes, name='buscar_clientes'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about_me, name='about_me'),
    path('pages/', views.blog_list, name='blog_list'),
    path('pages/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
