from django.test import TestCase
from django.contrib.auth.models import User
from tareas.models import Tareas

class TareasModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.tarea = Tareas.objects.create(
            nombre='Test Tarea',
            descripcion='Descripción de prueba',
            estado='TO DO',
            prioridad='MEDIO',
            fecha_entrega='2024-07-15',
            usuario_asignado=self.user
        )
    
    def test_crear_tarea(self):
        self.assertEqual(self.tarea.nombre, 'Test Tarea')
        self.assertEqual(self.tarea.estado, 'TO DO')
        self.assertEqual(self.tarea.usuario_asignado.username, 'testuser')
