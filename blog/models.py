from django.db import models
from django.utils.text import slugify


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    contenido = models.TextField()
    resumen = models.CharField(max_length=300, help_text='Breve descripción del artículo')
    imagen = models.ImageField(upload_to='blog/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo