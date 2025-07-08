from rest_framework.test import APITestCase
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from machine.models import Machine
from maintenance_worker.models import MaintenanceWorker


class OrdersAPITests(APITestCase):

    #set up by creating a user, machine, worker, and setting the orders endpoint
    def setUp(self):
        self.user = User.objects.create_user(username='M1235', password='123')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.machine = Machine.objects.create(
            name="Lathe X300",
            location="Sector A",
            status='O'
        )

        self.worker = MaintenanceWorker.objects.create(
            worker_name="Carlos Silva",
            worker_role="Técnico Mecânico"
        )
        self.url = '/order/'

    #test accessing orders endpoint without passing credentials in the header
    def test_no_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #test accessing orders endpoint with credentials in the header
    def test_get_orders_with_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #test creating an order with credentials in the header
    def test_create_order_with_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {
            "fk_machine": self.machine.id,
            "fk_maintenance_worker": self.worker.id,
            "order_description": "Trocar filtro",
            "order_type": "P",
            "order_status": "O"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["order_description"], "Trocar filtro")
