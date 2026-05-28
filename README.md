# 🎨 Portafolio Personal — Django

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Portafolio personal construido con **Django** que reúne mi presentación, proyectos, habilidades, blog y formulario de contacto en un solo lugar.

> 🚧 Proyecto en desarrollo activo — este README se actualiza a medida que el portafolio crece.

---

## 📋 Tabla de contenidos

- [Demo](#-demo)
- [Características](#-características)
- [Stack tecnológico](#-stack-tecnológico)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Variables de entorno](#-variables-de-entorno)
- [Comandos útiles](#-comandos-útiles)
- [Roadmap](#-roadmap)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

---

## 🌐 Demo

> ⚠️ Pendiente de despliegue. Próximamente disponible en producción.

---

## ✨ Características

- 👤 **Sobre mí** — presentación personal con biografía y foto
- 💼 **Proyectos** — catálogo de proyectos con imagen, tecnologías, demo y repositorio
- 🛠️ **Habilidades** — listado visual de tecnologías y herramientas dominadas
- ✍️ **Blog** — artículos personales sobre tecnología y aprendizaje
- 📬 **Contacto** — formulario funcional para recibir mensajes
- 🔐 **Panel de administración** — gestión de contenido sin tocar código (Django Admin)
- 📱 **Responsive** — adaptado a móvil, tablet y escritorio

---

## 🧰 Stack tecnológico

| Capa | Tecnología |
|------|------------|
| Backend | Python 3.11+, Django 5.0 |
| Base de datos | SQLite (desarrollo) |
| Frontend | HTML5, CSS3, JavaScript |
| Gestión de imágenes | Pillow |
| Configuración | python-decouple |
| Control de versiones | Git + GitHub |

---

## 📁 Estructura del proyecto

```
portafolio/
├── portafolio/           # Configuración global del proyecto
│   ├── settings.py       # Ajustes principales
│   ├── urls.py           # Rutas raíz
│   └── wsgi.py
├── core/                 # App: inicio, sobre mí, habilidades
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/core/
├── proyectos/            # App: catálogo de proyectos
├── blog/                 # App: artículos
├── contacto/             # App: formulario de contacto
├── templates/            # Templates compartidos (base.html)
├── static/               # CSS, JS, imágenes del diseño
├── media/                # Archivos subidos por el admin
├── manage.py             # CLI de Django
├── requirements.txt      # Dependencias del proyecto
├── .env.example          # Ejemplo de variables de entorno
├── .gitignore
└── README.md
```

---

## ⚙️ Requisitos previos

Antes de empezar, asegúrate de tener instalado:

- [Python 3.11 o superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Un editor de código (recomendado: [VS Code](https://code.visualstudio.com/))

Verifica las instalaciones:

```bash
python --version
git --version
```

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el archivo de ejemplo y completa los valores:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Edita `.env` con tus valores (ver sección [Variables de entorno](#-variables-de-entorno)).

### 5. Aplicar migraciones de la base de datos

```bash
python manage.py migrate
```

### 6. Crear un superusuario (admin)

```bash
python manage.py createsuperuser
```

### 7. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre tu navegador en **http://127.0.0.1:8000**

Panel de administración disponible en **http://127.0.0.1:8000/admin**

---

## 🔧 Uso

### Agregar contenido

1. Accede al panel admin en `/admin` con tu superusuario
2. Crea proyectos, artículos del blog y demás contenido
3. Las imágenes se guardan en `media/` automáticamente

### Modificar el diseño

- Estilos globales: `static/css/styles.css`
- Template base: `templates/base.html`
- Templates por sección: `<app>/templates/<app>/`

---

## 🔐 Variables de entorno

Crea un archivo `.env` en la raíz del proyecto basado en `.env.example`:

```env
# Modo debug (True en desarrollo, False en producción)
DEBUG=True

# Clave secreta de Django (¡genera una nueva en producción!)
SECRET_KEY=tu-clave-super-secreta-aqui

# Hosts permitidos (separados por coma)
ALLOWED_HOSTS=127.0.0.1,localhost
```

> 🔒 **Nunca subas el archivo `.env` a GitHub.** Ya está incluido en `.gitignore`.

Para generar una nueva `SECRET_KEY`:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 💻 Comandos útiles

| Comando | Descripción |
|---------|-------------|
| `python manage.py runserver` | Inicia el servidor de desarrollo |
| `python manage.py makemigrations` | Genera archivos de migración tras cambiar modelos |
| `python manage.py migrate` | Aplica las migraciones a la base de datos |
| `python manage.py createsuperuser` | Crea un usuario administrador |
| `python manage.py collectstatic` | Recopila archivos estáticos para producción |
| `python manage.py shell` | Abre una consola interactiva con Django cargado |
| `pip freeze > requirements.txt` | Actualiza el archivo de dependencias |

---

## 🗺️ Roadmap

- [x] Configuración inicial del proyecto
- [x] Apps principales creadas (core, proyectos, blog, contacto)
- [ ] Modelos de datos completos
- [ ] Diseño responsive del frontend
- [ ] Formulario de contacto funcional con envío de emails
- [ ] Sistema de comentarios en el blog
- [ ] Modo oscuro
- [ ] Despliegue en producción
- [ ] Integración con Google Analytics
- [ ] SEO optimizado (sitemap, meta tags)

---

## 🤝 Contribuir

Este es un proyecto personal, pero las sugerencias son bienvenidas. Si encuentras un bug o tienes una idea:

1. Abre un *issue* describiendo el problema o propuesta
2. Si quieres enviar código:
   - Haz fork del repositorio
   - Crea una rama: `git checkout -b mejora/nombre-descriptivo`
   - Haz tus commits con mensajes claros
   - Abre un *Pull Request*

---

## 📄 Licencia

Distribuido bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

---

## 📬 Contacto

**Tu Nombre** — [@tu_usuario](https://github.com/tu_usuario)

📧 tu.email@ejemplo.com

🔗 Link del proyecto: [https://github.com/TU_USUARIO/TU_REPOSITORIO](https://github.com/TU_USUARIO/TU_REPOSITORIO)

---

<p align="center">Hecho con ❤️ y Django</p>
