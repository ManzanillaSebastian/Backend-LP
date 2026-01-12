from rest_framework import serializers
from .models import Evento, Estudiante, Inscripcion

class EventoSerializer(serializers.ModelSerializer):
    cupos_disponibles = serializers.SerializerMethodField()

    class Meta:
        model = Evento
        fields = "__all__"

    def get_cupos_disponibles(self, obj):
        return obj.cupos_disponibles()

    def validate(self, data):
        hora_inicio = data.get('hora_inicio')
        hora_fin = data.get('hora_fin')

        if hora_inicio and hora_fin:
            if hora_fin <= hora_inicio:
                raise serializers.ValidationError(
                    "La hora de fin debe ser mayor que la hora de inicio."
                )

        return data

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"


class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = ["id", "estudiante", "evento"]

    def validate(self, data):
        evento = data["evento"]
        estudiante = data["estudiante"]

        if evento.cupos_disponibles() <= 0:
            raise serializers.ValidationError("No hay cupos disponibles para este evento.")

        if Inscripcion.objects.filter(evento=evento, estudiante=estudiante).exists():
            raise serializers.ValidationError("El estudiante ya está inscrito en este evento.")

        return data