from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from users.models import RatingScore
from users.permissions import IsAdminOrReadOnly
from users.serializers import RatingWriteSerializer, RatingReadSerializer
from movie.models import Movie, Genre
from movie.serializers import (
    MovieDetailSerializer,
    MovieListSerializer,
)
from main.utils import DefaultPaginator


class RatingAPIView(ListCreateAPIView):
    pagination_class = DefaultPaginator
    model = RatingScore
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.request.resolver_match.kwargs['slug']
        return self.model.objects.filter(movie__slug=slug)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return RatingReadSerializer
        elif self.request.method.lower() == 'post':
            return RatingWriteSerializer

    def get_serializer_context(self):
        # work around for proper versioning
        context = super().get_serializer_context()
        context['request'].version = self.request.resolver_match.kwargs['version']
        return context


class MovieViewSet(ModelViewSet):
    model = Movie
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPaginator
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    api_version = 'v1'

    def get_serializer_class(self):
        if self.request.method.lower() == 'get' \
                and self.request.build_absolute_uri(self.request.path) == reverse('movie-list', request=self.request):
            return MovieListSerializer
        else:
            return super(MovieViewSet, self).get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset().with_rating()
        keyword = self.request.GET.get('search')
        if keyword is not None:
            queryset = queryset.search(keyword)
        return queryset

    @action(detail=True, methods=['GET', 'POST'])
    def ratings(self, request, **kwargs):
        view = RatingAPIView.as_view()
        return view(request._request)


class GenreMoviesMoviesApiListView(ListCreateAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        genre = Genre.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        return genre.movie_set.all()
