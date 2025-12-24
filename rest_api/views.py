from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer

class EventoListCreateView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer