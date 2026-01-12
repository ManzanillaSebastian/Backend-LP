from django.db import models
from django.core.exceptions import ValidationError

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()

    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    cupo_maximo = models.PositiveIntegerField()

    def clean(self):
        if self.hora_inicio and self.hora_fin:
            if self.hora_fin <= self.hora_inicio:
                raise ValidationError(
                    "La hora de fin debe ser mayor que la hora de inicio."
                )

    def cupos_disponibles(self):
        return self.cupo_maximo - self.inscripciones.count()

    def __str__(self):
        return self.titulo

class Estudiante(models.Model):
    matricula = models.CharField(max_length=9, unique=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.matricula})"

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )

    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )

    class Meta:
        unique_together = ("estudiante", "evento")

    def __str__(self):
        return f"{self.estudiante} -> {self.evento}"