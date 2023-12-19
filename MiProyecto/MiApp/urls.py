from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.HomePageView.as_view(), name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('categorias/', views.CategoriasView.as_view(), name='categorias'),
    path('procesar-categoria/', views.procesar_categoria, name='procesar_categoria'),
    path('categorias/', views.CategoriasView.as_view(), name='categoria'),
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('procesar-producto/', views.procesar_producto, name='procesar_producto'),
    path('procesar-cliente/', views.procesar_cliente, name='procesar_cliente'),
    path('cliente/', views.cliente_list, name='cliente_list'),
    path('cliente/', views.cliente_list, name='cliente'),  
    path('buscar-clientes/', views.buscar_clientes, name='buscar_clientes'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)