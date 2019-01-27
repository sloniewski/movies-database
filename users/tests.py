import json

from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

User = get_user_model()


class TestAuth(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_username = 'duffy'
        self.test_password = 'duck'
        self.user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        self.token = Token.objects.create(user=self.user)

    def test_token_auth(self):
        url = reverse('users:token-auth')
        data = {
            'username': self.test_username,
            'password': self.test_password,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['token'], self.token.key)
