import json

from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from movie.models import Movie
from users.models import WatchList, WatchListEntry

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
    api_version = 'api-v1'

    def setUp(self):
        super().setUp()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.watchlist = WatchList.objects.create(name='some name', user=self.user)
        self.movie = Movie.objects.create(
            title='test title',
            year=2001,
            description='lorem ipsum',
        )
        self.movie_2 = Movie.objects.create(
            title='another title',
            year=2007,
            description='bacon ipsum',
        )
        self.entry = WatchListEntry.objects.create(list=self.watchlist, movie=self.movie)

    def test_watchlist_get(self):
        url = reverse(self.api_version + ':watchlist-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_watchlist_detail_get(self):
        url = reverse(self.api_version + ':watchlist-detail', kwargs={'slug': self.watchlist.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], self.watchlist.name)

    def test_watchlist_post(self):
        url = reverse(self.api_version + ':watchlist-list')
        data = {
            'name': 'test list',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_entries_get(self):
        url = reverse(self.api_version + ':watchlist-entry-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_entry_delete(self):
        retained_id = self.entry.id
        url = reverse(
            self.api_version + ':watchlist-entry-detail',
            kwargs={'pk': self.entry.id}
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(WatchList.DoesNotExist):
            WatchList.objects.get(id=retained_id)

    def test_entry_post(self):
        url = reverse(self.api_version + ':watchlist-entry-list')
        data = {
            'list': self.watchlist.slug,
            'movie': self.movie_2.slug,
        }
        reponse = self.client.post(url, data, format='json')
        self.assertEqual(reponse.status_code, 201)
