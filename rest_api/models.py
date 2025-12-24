from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()

    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    cupo_maximo = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

    def horario(self):
        if self.hora_inicio and self.hora_fin:
            return f"{self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"
        return "Horario no definido"

    def clean(self):
        if self.hora_inicio and self.hora_fin:
            if self.hora_fin <= self.hora_inicio:
                raise ValidationError(
                    "La hora de fin debe ser mayor que la hora de inicio."
                )