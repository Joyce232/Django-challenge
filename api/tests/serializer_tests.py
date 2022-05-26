from rest_framework.test import APITestCase
from rest_framework import status


class SerializersTestCase(APITestCase):

    def test_email_validation(self):
        user = {'first_name': 'Fátima', 'last_name': 'Franco', 'email': 'fa@email.com',
                'username': 'fafa35', 'password': 'senha-super-secreta22'}
        self.client.post("/api/register/", user)

        user2 = {'first_name': 'Fábio', 'las_name': 'Almeida', 'email': 'fa@email.com',
                 'username': 'euofabio', 'password': 'senha-d0-fabio'}
        response = self.client.post("/api/register/", user2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_username_validation(self):
        user = {'first_name': 'Marshall', 'last_name': 'Mathers', 'email': 'email@email.com',
                'username': 'slim_shady', 'password': 'senha-super-secreta22'}
        self.client.post("/api/register/", user)

        new_user = {'first_name': 'Eminem', 'last_name': 'Mathers', 'email': 'ememail@email.com',
                    'username': 'slim_shady', 'password': 'senha-super-secreta23'}
        response = self.client.post("/api/register/", new_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_article_validation(self):
        author = {'id': '64ebedc6-3432-4d14-948e-48ef319ecdbf', 'name': 'super eyepatch wolf'}
        response = self.client.post("/api/authors/", author)
        if response.status_code == status.HTTP_201_CREATED:
            article = {'author_id': '64ebedc6-3432-4d14-948e-48ef319ecdbf', 'category': 'teste',
                       'title': 'Teste de validação', 'summary': 'bbb', 'fisrt_paragraph': '[REDACTED]',
                       'body': 'not fifty'}
            article_response = self.client.post("/api/articles/", article)
            self.assertEqual(article_response.status_code, status.HTTP_400_BAD_REQUEST)

