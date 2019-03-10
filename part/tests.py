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
    api_version = 'api-v1'

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
        url = reverse(self.api_version + ':crew-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cast_list_get(self):
        url = reverse(self.api_version + ':cast-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cast_list_post(self):
        url = reverse(self.api_version + ':cast-list')
        data = {
            'person': self.actor.pk,
            'movie': self.movie.slug,
            'character': 'very bad',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
