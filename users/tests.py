import json

from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


from .models import WatchList

User = get_user_model()


class BaseTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_username = 'duffy'
        self.test_password = 'duck'
        self.user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
        )
        self.token = Token.objects.create(user=self.user)


class TestAuth(BaseTest):

    def test_token_auth(self):
        url = reverse('users:token-auth')
        data = {
            'username': self.test_username,
            'password': self.test_password,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['token'], self.token.key)


class TestWatchList(BaseTest):

    def setUp(self):
        super().setUp()
        self.watchlist = WatchList.objects.create(name='some name', user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_watchlist_get(self):
        url = reverse('users:watchlist-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_watchilist_detail_get(self):
        url = reverse('users:watchlist-detail', kwargs={'slug': self.watchlist.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

