from django.test import TestCase
from tareas.models import Tareas
from tareas.serializers import TareaSerializer
from django.contrib.auth.models import User

class TareasSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.tarea = Tareas.objects.create(
            nombre='Test Tarea',
            descripcion='Descripción de prueba',
            estado='DOING',
            prioridad='ALTO',
            fecha_entrega='2024-07-20',
            usuario_asignado=self.user
        )
    
    def test_serializacion_tarea(self):
        serializer = TareaSerializer(self.tarea)
        data = serializer.data
        self.assertEqual(data['nombre'], 'Test Tarea')
        self.assertEqual(data['estado'], 'DOING')
        self.assertEqual(data['prioridad'], 'ALTO')
