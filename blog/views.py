from django.shortcuts import render, get_object_or_404
from .models import Articulo


def lista(request):
    articulos = Articulo.objects.filter(publicado=True)
    contexto = {
        'articulos': articulos,
    }
    return render(request, 'blog/lista.html', contexto)


def detalle(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug, publicado=True)
    contexto = {
        'articulo': articulo,
    }
    return render(request, 'blog/detalle.html', contexto)