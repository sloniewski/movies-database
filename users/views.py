import json

from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import View
from django.http import HttpResponse

from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    WatchListSerializer,
    WatchListDetailSerializer,
    WatchListEntrySerializer
)
from .models import WatchList, WatchListEntry


class LoginApiView(APIView):

    def get_login_fail_response(self):
        return HttpResponse(
            json.dumps(({'users': 'invalid login or password'})),
            content_type='application/json',
        )

    def post(self, request):
        try:
            credentials = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return self.get_login_fail_response()

        try:
            username = credentials['username']
            password = credentials['password']
        except KeyError:
            return self.get_login_fail_response()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(
                    json.dumps(({'users': 'login successful'})),
                    content_type='application/json',
                )
        else:
            return self.get_login_fail_response()


class WhoAmI(View):

    def get(self, request):
        response = HttpResponse()
        if request.user.is_authenticated:
            response.write(request.user.username)
        else:
            response.write('user is none')
        return response


class WatchListViewSet(ModelViewSet):
    serializer_class = WatchListDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'
    model = WatchList
    api_version = 'api-v1'

    def get_queryset(self):
        return WatchList.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get' and self.request.path == reverse('watchlist-list', request=self.request):
            return WatchListSerializer
        else:
            return super(WatchListViewSet, self).get_serializer_class()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class WatchListEntryViewSet(ModelViewSet):
    serializer_class = WatchListEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WatchListEntry.objects.filter(list__user=self.request.user)
