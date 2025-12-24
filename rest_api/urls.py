from django.urls import path
from . import views

urlpatterns = [
   path("", views.EventoListCreateView.as_view(), name="eventos"),
]