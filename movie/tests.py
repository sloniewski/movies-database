import json

from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from movie.models import Movie
from person.models import Person
from part.models import Cast


User = get_user_model()


class TestMovieViews(TestCase):
    api_version = 'v1'
    fixtures = [
        'fixtures/movie.json',
        'fixtures/person.json',
        'fixtures/part.json',
    ]

    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.first()

        self.test_username = 'duffy'
        self.test_password = 'duck'
        self.user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
            is_staff=True,
        )
        self.token = Token.objects.create(user=self.user)

    def test_get_list_movies(self):
        url = reverse('movie-list', kwargs={'version': self.api_version})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_post_movie(self):
        url = reverse('movie-list', kwargs={'version': self.api_version})
        data = {
            'title': 'huntin with elmer',
            'description': 'huntin rabbits',
            'year': 2003,
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_post_movie_401(self):
        url = reverse('movie-list', kwargs={'version': self.api_version})
        data = {
            'title': 'huntin with elmer',
            'description': 'huntin rabbits',
            'year': 2003,
        }
        self.client.credentials()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_post_movie_403(self):
        user = User.objects.create_user(
            username='abc',
            password='xyz',
            is_staff=False,
        )
        token = Token.objects.create(user=user)

        url = reverse('movie-list', kwargs={'version': self.api_version})
        data = {
            'title': 'huntin with elmer',
            'description': 'huntin rabbits',
            'year': 2003,
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 403)

    def test_movie_detail_get(self):
        url = reverse(
            viewname='movie-detail',
            kwargs={
                'slug': self.movie.slug,
                'version': self.api_version
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode('utf8')).get('title'), self.movie.title)
