from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MensajeForm


def formulario(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu mensaje fue enviado! Te responderé pronto.')
            return redirect('contacto:formulario')
    else:
        form = MensajeForm()

    contexto = {
        'form': form,
    }
    return render(request, 'contacto/formulario.html', contexto)