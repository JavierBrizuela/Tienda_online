# Tienda_online
Tienda online
Es una tienda online de uso general desarrollado en Django 4.1.1 sobre un template de bootstrap, 
En el cual pongo en practica la creacion de formularios, relaciones entre modelos, extension del modelo de usuarios, sesiones, plataforma 
de pagos con stripe.

Crear Entorno Virtual

# virtualenv mientorno
Activar Entorno Virtual Windows:

# ./mientorno/Scripts/activate
Linux:

# ./mientorno/Bin/activate
Clonar repositorio

(mientorno)# git clone https://github.com/JavierBrizuela/Tienda_online.git
Instalar Dependencias

(mientorno)# pip install -r requeriments.txt
Crear super usuario para administrar la base de datos En la carpeta del proyecto

python manage.py createsuperuser
Inicializar Server Django En la carpeta del proyecto

python manage.py runserver
