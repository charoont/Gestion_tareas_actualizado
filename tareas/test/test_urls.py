from django.test import TestCase
from django.urls import reverse

class TareasURLTestCase(TestCase):
    def test_urls_resuelven(self):
        url = reverse('tareas-list')
        self.assertEqual(url, '/api/tareas/')
