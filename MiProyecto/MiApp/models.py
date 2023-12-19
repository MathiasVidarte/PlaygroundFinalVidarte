from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    website_link = models.URLField(blank=True)

    # Modifica 'user_permissions' a 'customuser_permissions'
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')

    # Agrega un 'related_name' específico para este accessor inverso
    groups = models.ManyToManyField(Group, related_name='customuser_groups')


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
