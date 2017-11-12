from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response

from persons.models import Person
from persons.serializers import PersonSerializer


class PersonApiView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Person, pk=pk)

    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
