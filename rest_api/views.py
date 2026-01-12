from rest_framework import viewsets
from .models import Evento, Estudiante, Inscripcion
from .serializers import EventoSerializer, EstudianteSerializer, InscripcionSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    @action(detail=True, methods=["get"])
    def inscripciones(self, request, pk=None):
        evento = self.get_object()
        inscripciones = evento.inscripciones.all()
        serializer = InscripcionSerializer(inscripciones, many=True)
        return Response(serializer.data)

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer