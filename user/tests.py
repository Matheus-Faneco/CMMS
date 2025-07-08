from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserAuthTests(APITestCase):
    #set up by creating a user and generating JWT token
    def setUp(self):
        self.user = User.objects.create_user(username='A1234', password='senha123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    #test login with valid credentials at /api/token/
    def test_login_jwt(self):
        data = {
            "username": "A1234",
            "password": "123"
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    #test accessing protected route without token returns 401
    def test_protected_route_requires_auth(self):
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #test accessing protected route with valid token does not return 401
    def test_access_protected_route_with_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/order/')
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
