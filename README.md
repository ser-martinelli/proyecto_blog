# proyecto_blog
Proyecto requerido por CoderHouse en el curso de Python

Descripción:
Este proyecto consiste en una aplicación web desarrollada en Django utilizando el patrón MVT (Modelo-Vista-Template).
La aplicación simula un blog literario donde se pueden crear autores, categorías y publicaciones.

Se implementaron las siguientes funcionalidades:

Herencia de HTML:
Se utilizó un archivo base.html que contiene la estructura principal del sitio y del cual heredan todas las demás plantillas.

Modelos creados:
Se desarrollaron 3 modelos: autor, categoría y posteos.

Formularios:
Se implementaron formularios utilizando ModelForm para: crear autor, crear categoría y crear posteos.

Formularios de búsqueda:
Se implementó un formulario que permite buscar posts por título utilizando el método GET y filtros con icontains.