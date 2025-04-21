from rest_framework import viewsets, filters
from tareas.models import Tareas
from tareas.serializers import TareaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.select_related("usuario_asignado").order_by("fecha_entrega")
    serializer_class = TareaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['estado', 'fecha_entrega', 'usuario_asignado']
    search_fields = ['nombre']

    def perform_create(self, serializer):
        # Solo asignar el usuario autenticado si está logueado
        if self.request.user.is_authenticated:
            serializer.save(usuario_asignado=self.request.user)
        else:
            serializer.save()


