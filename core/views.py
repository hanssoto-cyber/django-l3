from django.shortcuts import render


def inicio(request):
    habilidades = {
        'lenguajes': [
            {'nombre': 'Python', 'nivel': 70, 'icono': '🐍'},
        ],
        'ciberseguridad': [
            {'nombre': 'Kali Linux', 'nivel': 65, 'icono': '🐉'},
            {'nombre': 'Wireshark', 'nivel': 60, 'icono': '🦈'},
            {'nombre': 'Nmap', 'nivel': 70, 'icono': '🔍'},
            {'nombre': 'Burp Suite', 'nivel': 55, 'icono': '🕷️'},
            {'nombre': 'Metasploit', 'nivel': 60, 'icono': '💥'},
            {'nombre': 'John the Ripper', 'nivel': 50, 'icono': '🔓'},
            {'nombre': 'Hydra', 'nivel': 50, 'icono': '🐍'},
        ],
        'herramientas': [
            {'nombre': 'VS Code', 'nivel': 85, 'icono': '💻'},
            {'nombre': 'Git', 'nivel': 70, 'icono': '🌿'},
            {'nombre': 'Docker', 'nivel': 55, 'icono': '🐋'},
        ],
    }

    stats = [
        {'valor': '24/7', 'label': 'Aprendiendo'},
        {'valor': '10+', 'label': 'Herramientas dominadas'},
        {'valor': '∞', 'label': 'Curiosidad'},
        {'valor': '0', 'label': 'Límites'},
    ]

    contexto = {
        'nombre': 'Hans Soto',
        'titulo': 'Blue Team Engineer',
        'subtitulo': 'Futuro Ingeniero en Ciberseguridad',
        'bio': 'Estudiante de ciberseguridad enfocado en defensa, análisis de tráfico y respuesta a incidentes. Apasionado por entender cómo funcionan los ataques para construir mejores defensas.',
        'habilidades': habilidades,
        'stats': stats,
    }
    return render(request, 'core/inicio.html', contexto)