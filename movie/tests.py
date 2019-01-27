import json

from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from movie.models import Movie


User = get_user_model()


class TestMovieViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title='bugs bunny',
            description='carrots are great',
            year=2001,
        )

        self.test_username = 'duffy'
        self.test_password = 'duck'
        self.user = User.objects.create_user(
            username=self.test_username,
            password=self.test_password,
            is_staff=True,
        )
        self.token = Token.objects.create(user=self.user)

    def test_get_list_movies(self):
        url = reverse('movie:movie-list')
        response = self.client.get(url)
        self.assertEqual(
            json.loads(response.content).pop().get('title'), 'bugs bunny')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_post_movie(self):
        url = reverse('movie:movie-list')
        data = {
            'title': 'huntin with elmer',
            'description': 'huntin rabbits',
            'year': 2003,
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
