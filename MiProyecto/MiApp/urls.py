from django.urls import path
from .views import categoria, producto, cliente

urlpatterns = [
    path('categoria/', categoria, name='categoria'),
    path('producto/', producto, name='producto'),
    path('cliente/', cliente, name='cliente'),
]
