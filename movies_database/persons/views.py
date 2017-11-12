from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response

from persons.models import Person
from persons.serializers import PersonSerializer


class PersonApiView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Person, pk=pk)

    def get(self, request, pk):
        person = self.get_object(pk)
        print(person)
        serializer = PersonSerializer(person, context={'request': request})
        return Response(serializer.data)
