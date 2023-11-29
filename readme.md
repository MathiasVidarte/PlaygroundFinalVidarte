# MiProyecto

Este es un proyecto web Django con el patrón MVT que incluye:

- Herencia de HTML.
- Tres clases en models: `Categoria`, `Producto`, `Cliente`.
- Formularios para insertar datos en cada modelo.
- Un formulario para buscar en la base de datos.

## Instrucciones de prueba

1. Asegúrate de tener Python y Django instalados.
2. Clona el repositorio desde GitHub: `git clone https://github.com/TU_USUARIO/TU_REPO.git`
3. Instala los requisitos: `pip install -r requirements.txt`
4. Realiza las migraciones: `python manage.py makemigrations` y `python manage.py migrate`
5. Inicia el servidor: `python manage.py runserver`
6. Visita las siguientes URL en tu navegador:
   - http://localhost:8000/miapp/categoria/
   - http://localhost:8000/miapp/producto/
   - http://localhost:8000/miapp/cliente/
