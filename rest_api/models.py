from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha = models.DateField()
    cupos = models.IntegerField()

    def __str__(self):
        return self.titulo