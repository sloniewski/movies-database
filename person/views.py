from django.urls import reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from person.models import Person
from person.serializers import PersonDetailSerializer, PersonListSerializer
from main.utils import DefaultPaginator
from users.permissions import IsAdminOrReadOnly


class PersonViewSet(ModelViewSet):
    model = Person
    serializer_class = PersonDetailSerializer
    pagination_class = DefaultPaginator
    queryset = Person.objects.all().prefetch_related('cast_member')
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'
    api_version = 'api-v1'

    def get_serializer_class(self):
        if self.request.method.lower() == 'get' and self.request.path == reverse(self.api_version + ':person-list'):
            return PersonListSerializer
        else:
            return super(PersonViewSet, self).get_serializer_class()
            

