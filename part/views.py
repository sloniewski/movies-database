from rest_framework.viewsets import ModelViewSet

from part.models import Cast, Crew
from part.serializers import (
    CastSerializer,
    CrewSerializer,
)

class CastView(ModelViewSet):
    model = Cast
    serializer_class = CastSerializer
    queryset = Cast.objects.all()


class CrewView(ModelViewSet):
    model = Crew
    serializer_class = CrewSerializer
    queryset = Crew.objects.all()
