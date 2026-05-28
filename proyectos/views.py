from django.shortcuts import render, get_object_or_404
from .models import Proyecto


def lista(request):
    proyectos = Proyecto.objects.all()
    contexto = {
        'proyectos': proyectos,
    }
    return render(request, 'proyectos/lista.html', contexto)


def detalle(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    contexto = {
        'proyecto': proyecto,
    }
    return render(request, 'proyectos/detalle.html', contexto)