from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, EstudianteViewSet, InscripcionViewSet

router = DefaultRouter()
router.register(r"eventos", EventoViewSet)
router.register(r"estudiantes", EstudianteViewSet)
router.register(r"inscripciones", InscripcionViewSet)

urlpatterns = router.urls