from rest_framework.test import APITestCase
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class MachineTests(APITestCase):
    #set up by creating a user and setting the machine endpoint
    def setUp(self):
        self.user = User.objects.create_user(username='M1235', password='123')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.url = '/machine/'

    #test accessing the endpoint without passing credentials in the header
    def test_no_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)

    #test with credentials in the header
    def test_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
