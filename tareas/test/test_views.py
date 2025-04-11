from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from tareas.models import Tareas

class TareasAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.tarea = Tareas.objects.create(
            nombre='API Test Tarea',
            descripcion='Descripción de prueba',
            estado='BACKLOG',
            prioridad='BAJA',
            fecha_entrega='2024-07-25',
            usuario_asignado=self.user
        )
        self.url = reverse('tareas-list')

    def test_obtener_lista_tareas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_tarea_api(self):
        data = {
            'nombre': 'Nueva Tarea',
            'descripcion': 'Nueva descripción',
            'estado': 'TO DO',
            'prioridad': 'MEDIO',
            'fecha_entrega': '2024-07-30',
            'usuario_asignado': self.user.id  # <- ESTE CAMPO ES EL CLAVE
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

