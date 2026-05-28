from django.db import models


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    url_demo = models.URLField(blank=True)
    url_github = models.URLField(blank=True)
    tecnologias = models.CharField(
        max_length=300,
        help_text='Tecnologías separadas por comas. Ej: Python, Django, HTML'
    )
    fecha_creacion = models.DateField(auto_now_add=True)
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.titulo
