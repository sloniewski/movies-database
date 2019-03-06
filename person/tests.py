import json

from django.shortcuts import reverse
from django.test import TestCase
from rest_framework.test import APIClient

from person.models import Person


class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(
            first_name='Wile E.',
            second_name='Coyote',
            year_of_birth='1949',
        )

    def test_person_list_get(self):
        url = reverse('person:person-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            json.loads(response.content)['results'].pop().get('first_name'),
            self.person.first_name
        )

    def test_person_detail_get(self):
        url = reverse('person:person-detail', kwargs={'pk': self.person.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            json.loads(response.content).get('first_name'),
            self.person.first_name
        )

    def test_person_list_post(self):
            url = reverse('person:person-list')
            data = {
                'first_name': 'Elmer',
                'second_name': 'Fudd',
                'year_of_birth': '1949',
            }
            self.client.credentials()
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, 401)
