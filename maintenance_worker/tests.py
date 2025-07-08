from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User

class MaintenanceWorkerTests(APITestCase):

    #set up by creating a user and setting the maintenance worker endpoint
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.url = '/maintenance_worker/'

    # test accessing the endpoint without passing credentials in the header
    def test_list_requires_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    # test accessing the endpoint with credentials and creating a worker
    def test_create_worker_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            "worker_name": "João",
            "worker_role": "Técnico"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["worker_name"], "João")
