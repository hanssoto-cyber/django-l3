from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import MensajeForm


def formulario(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            # 1. Guardar el mensaje en la base de datos
            mensaje = form.save()

            # 2. Enviar email de notificación
            try:
                asunto_email = f'[Portafolio] Nuevo mensaje: {mensaje.asunto}'
                cuerpo_email = (
                    f'Has recibido un nuevo mensaje desde tu portafolio.\n\n'
                    f'De: {mensaje.nombre}\n'
                    f'Email: {mensaje.email}\n'
                    f'Asunto: {mensaje.asunto}\n\n'
                    f'Mensaje:\n{mensaje.mensaje}\n'
                )
                send_mail(
                    asunto_email,
                    cuerpo_email,
                    settings.EMAIL_HOST_USER,        # remitente
                    [settings.EMAIL_DESTINATARIO],   # destinatario (tú)
                    fail_silently=False,
                )
                messages.success(
                    request,
                    '¡Tu mensaje fue enviado! Te responderé pronto.'
                )
            except Exception as e:
                # Si falla el email, el mensaje igual se guardó en BD
                messages.warning(
                    request,
                    'Tu mensaje se guardó correctamente. ¡Gracias por escribir!'
                )

            return redirect('contacto:formulario')
    else:
        form = MensajeForm()

    contexto = {
        'form': form,
    }
    return render(request, 'contacto/formulario.html', contexto)