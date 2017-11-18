from django.shortcuts import get_object_or_404
from django.db.models import ObjectDoesNotExist

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response
from rest_framework import status

from persons.models import Person
from persons.serializers import PersonDetailSerializer, PersonListSerializer


class DefaultPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PersonApiView(APIView):
    serializer_class = PersonDetailSerializer
    model = Person

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = self.serializer_class(person, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            person = self.get_object(pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class PersonsListApiView(ListAPIView):
    serializer_class = PersonListSerializer
    pagination_class = DefaultPaginator

    def get_queryset(self):
        return Person.objects.all()

    def post(self, request):
        serializer = PersonDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
