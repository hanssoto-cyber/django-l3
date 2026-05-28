from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@email.com'}),
            'asunto': forms.TextInput(attrs={'placeholder': '¿De qué se trata?'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...', 'rows': 5}),
        }