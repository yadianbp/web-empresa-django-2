from django.db import models

# Create your models here.


class Service(models.Model):
    Title = models.CharField(max_length=200, verbose_name='Titulo')
    Subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    Content = models.TextField(verbose_name='Contenido')
    Image = models.ImageField(verbose_name='Imagen', upload_to='services')
    Created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')
    Updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizacion')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-Created']

    def __str__(self):
        return self.Title