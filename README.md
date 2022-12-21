# aat_ong_com-1_g-2
Blog para ONG Amigos del Arte y Turismo JJ Castelli

## Dependencias
- Django 3.2
- Pillow
- Python-dotenv

## Comenzando
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate

## Crear super usuario para administrar el blog
- python manage.py createsuperuser

## Lanzar
- python manage.py runserver

## Visualizar
- Local
  - http://localhost:8000 or http://127.0.0.1:8000
- Online
  - https://montexbjeliseo.pythonanywhere.com/

## Aclaraciones
- La base de datos de la demo __no__ está en este repositorio. Por lo tanto al correr en __local__ tendrá que cargar sus propios recursos(crear usuarios, noticias, etc).
