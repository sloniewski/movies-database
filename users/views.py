import json

from django.contrib.auth import authenticate, login
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import WatchListSerializer, WatchListEntrySerializer
from .permissions import IsUserOrReadOnly
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
    serializer_class = WatchListSerializer
    permission_classes = [IsUserOrReadOnly]
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return WatchList.objects.all()


class WatchListEntryViewSet(ModelViewSet):
    serializer_class = WatchListEntrySerializer
    permission_classes = [IsUserOrReadOnly]

    def get_queryset(self):
        return WatchListEntry.objects.all()
