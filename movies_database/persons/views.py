from django.db.models import ObjectDoesNotExist

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from persons.models import Person
from persons.serializers import PersonDetailSerializer, PersonListSerializer


class DefaultPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class PersonViewSet(GenericViewSet):
    model = Person
    serializer_class = PersonDetailSerializer
    pagination_class = DefaultPaginator
    queryset = Person.objects.all()

    def retrieve(self, request, pk):
        try:
            instance = self.get_object()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(
            instance=instance,
        )
        return Response(serializer.data)

    def create(self, response):
        serializer = PersonDetailSerializer(data=self.request.data)
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

    def list(self, request):
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(
            self.queryset,
            self.request,
            view=self
        )
        serializer = PersonListSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)



    def partial_update(self,request, pk):
        try:
            person = self.get_object()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        movie = self.get_object()
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        try:
            person = self.get_object()
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_204_NO_CONTENT)
