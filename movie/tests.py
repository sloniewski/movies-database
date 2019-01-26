import json

from django.shortcuts import reverse
from django.test import TestCase

from rest_framework.test import APIClient

from movie.models import Movie


class TestMovieViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title='bugs bunny',
            description='carrots are great',
            year=2001,
        )

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
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
