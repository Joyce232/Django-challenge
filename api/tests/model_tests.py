from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Author


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'first_name': 'sushi', 'last_name': 'santana', 'email': 'sushi@email.com',
                'username': 'delinquente', 'password': 'oitonumeros'}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_str_function(self):
        author = Author.objects.create(name='Fiódor Dostoiévski')
        self.assertEqual(str(author), 'Fiódor Dostoiévski')
