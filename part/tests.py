import json

from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from movie.models import Movie
from person.models import Person
from part.models import Cast, Crew


User = get_user_model()


class TestMovieViews(TestCase):
    api_version = 'v1'
    fixtures = [
        'fixtures/movie.json',
        'fixtures/person.json',
        'fixtures/part.json'
    ]

    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title='bugs bunny',
            description='carrots are great',
            year=2001,
        )
        self.user = User.objects.create_user(
            username='duffy',
            password='duck',
            is_staff=True,
        )
        self.token = Token.objects.create(user=self.user)
        self.person = Person.objects.create(
            first_name='test_1', second_name='test_2',
            year_of_birth=1973
        )
        self.actor = Cast.objects.create(
            person=self.person, movie=self.movie,
            character='testing'
        )
        self.director = Crew.objects.create(
            person=self.person, movie=self.movie,
            credit='director',
        )

    def test_crew_list_get(self):
        url = reverse('crew-list', kwargs={'version': self.api_version})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_crew_list_post_401(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 12345')
        url = reverse('crew-list', kwargs={'version': self.api_version})
        data = {
            'person': {
                'slug': self.person.slug,
            },
            'movie': {
                'slug': self.movie.slug,
            },
            'credit': 'very bad',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_crew_list_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('crew-list', kwargs={'version': self.api_version})
        data = {
            'person': {
                'slug': self.person.slug,
            },
            'movie': {
                'slug': self.movie.slug,
            },
            'credit': 'very bad',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_cast_list_get(self):
        url = reverse('cast-list', kwargs={'version': self.api_version})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cast_list_post_401(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 12345')
        url = reverse('crew-list', kwargs={'version': self.api_version})
        data = {
            'person': {
                'slug': self.person.slug,
            },
            'movie': {
                'slug': self.movie.slug,
            },
            'credit': 'very bad',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_cast_list_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('cast-list', kwargs={'version': self.api_version})
        data = {
            'person': {
                'slug': self.person.slug,
            },
            'movie': {
                'slug': self.movie.slug,
            },
            'character': 'very bad',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
