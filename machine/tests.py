from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Machine

class MachineTests(APITestCase):
    #Teste de Adição de máquina
    def test_add_machine(self):
        url = reverse('machine-list')
        data = {
            "name": "Compressor A",
            "location": "Fábrica 1",
            "status": "O"
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Machine.objects.count(), 1)
        self.assertEqual(Machine.objects.get().name, 'Compressor A')

