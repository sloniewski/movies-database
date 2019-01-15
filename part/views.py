from rest_framework.viewsets import ModelViewSet

from main.utils import DefaultPaginator

from part.models import Cast, Crew
from part.serializers import (
    CastSerializer,
    CrewSerializer,
)


class CastView(ModelViewSet):
    model = Cast
    serializer_class = CastSerializer
    queryset = Cast.objects.all().select_related('movie').select_related('person')
    pagination_class = DefaultPaginator


class CrewView(ModelViewSet):
    model = Crew
    serializer_class = CrewSerializer
    queryset = Crew.objects.all().select_related('movie').select_related('person')
    pagination_class = DefaultPaginator
