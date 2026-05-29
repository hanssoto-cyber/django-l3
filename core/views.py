from django.shortcuts import render


def inicio(request):
    # Áreas de competencia (conectadas con tus labs reales)
    competencias = [
        {
            'icono': '🛡️',
            'titulo': 'Monitoreo & SIEM',
            'descripcion': 'Detección de amenazas en tiempo real, análisis de logs y gestión de eventos de seguridad.',
            'tags': ['ELK Stack', 'Kibana', 'Logstash'],
        },
        {
            'icono': '🌐',
            'titulo': 'Seguridad de Redes',
            'descripcion': 'Segmentación, hardening de infraestructura y configuración defensiva de redes empresariales.',
            'tags': ['Cisco', 'VLANs', 'OSPF', 'NAT'],
        },
        {
            'icono': '🔍',
            'titulo': 'Análisis de Tráfico',
            'descripcion': 'Inspección de paquetes, detección de anomalías y reconocimiento de patrones de ataque.',
            'tags': ['Wireshark', 'Nmap', 'tcpdump'],
        },
        {
            'icono': '📋',
            'titulo': 'Respuesta a Incidentes',
            'descripcion': 'Documentación de incidentes bajo estándares y flujos de trabajo de analista SOC.',
            'tags': ['NIST SP 800-61', 'SOC L1', 'Triaje'],
        },
        {
            'icono': '🖥️',
            'titulo': 'Administración de Sistemas',
            'descripcion': 'Gestión de servidores Windows y Linux, servicios de directorio y dominio corporativo.',
            'tags': ['Windows Server', 'Linux', 'Active Directory'],
        },
        {
            'icono': '⚙️',
            'titulo': 'Automatización',
            'descripcion': 'Scripting para automatizar tareas de seguridad, análisis y procesamiento de datos.',
            'tags': ['Python', 'Bash'],
        },
    ]

    # Stack tecnológico (grilla limpia, sin niveles)
    stack = [
        {'nombre': 'Python', 'icono': '🐍'},
        {'nombre': 'Kali Linux', 'icono': '🐉'},
        {'nombre': 'Wireshark', 'icono': '🦈'},
        {'nombre': 'Nmap', 'icono': '🔍'},
        {'nombre': 'Burp Suite', 'icono': '🕷️'},
        {'nombre': 'Metasploit', 'icono': '💥'},
        {'nombre': 'ELK Stack', 'icono': '📊'},
        {'nombre': 'Cisco PT', 'icono': '🌐'},
        {'nombre': 'VS Code', 'icono': '💻'},
        {'nombre': 'Git', 'icono': '🌿'},
        {'nombre': 'Docker', 'icono': '🐋'},
        {'nombre': 'VMware', 'icono': '🖧'},
    ]

    stats = [
        {'valor': '4', 'label': 'Proyectos'},
        {'valor': '3', 'label': 'Labs SOC'},
        {'valor': '2°', 'label': 'Año cursando'},
        {'valor': '∞', 'label': 'Ganas de aprender'},
    ]

    contexto = {
        'nombre': 'Hans Soto',
        'titulo': 'Analista SOC en formación',
        'subtitulo': 'Futuro Ingeniero en Ciberseguridad',
        'bio': 'Estudiante de ciberseguridad enfocado en defensa, análisis de tráfico y respuesta a incidentes. Apasionado por entender cómo funcionan los ataques para construir mejores defensas.',
        'competencias': competencias,
        'stack': stack,
        'stats': stats,
    }
    return render(request, 'core/inicio.html', contexto)

def error_404(request, exception):
    return render(request, '404.html', status=404)