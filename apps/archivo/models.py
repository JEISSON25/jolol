from django.db import models

class Archivo(models.Model):
    archivo = models.FileField(upload_to='files/', blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo - {self.archivo.name}"