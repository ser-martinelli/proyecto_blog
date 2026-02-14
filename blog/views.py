
from django.shortcuts import render
from .models import Autor, Categoria, Post
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario


def inicio(request):
    posts = Post.objects.all()
    return render(request, "blog/inicio.html", {"posts": posts})


def crear_autor(request):
    if request.method == "POST":
        form = AutorFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorFormulario()
    return render(request, "blog/crear_autor.html", {"form": form})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaFormulario()
    return render(request, "blog/crear_categoria.html", {"form": form})


def crear_post(request):
    if request.method == "POST":
        form = PostFormulario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostFormulario()
    return render(request, "blog/crear_post.html", {"form": form})



def buscar_post(request):
    resultados = None

    if request.method == "GET":
        titulo = request.GET.get("titulo")

        if titulo:
            resultados = Post.objects.filter(titulo__icontains=titulo)

    return render(request, "blog/buscar.html", {
        "resultados": resultados
    })

