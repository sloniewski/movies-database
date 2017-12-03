from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View

from rest_framework.views import APIView

import json


class LoginApiView(APIView):

    def post(self, request):
        try:
            credentials = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponse(
                json.dumps(({'users': 'invalid login or password'})),
                content_type='application/json',
            )
        username = credentials['username']
        password = credentials['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(
                    json.dumps(({'users': 'login successful'})),
                    content_type='application/json',
                )
        else:
            return HttpResponse(
                json.dumps(({'users': 'invalid login or password'})),
                content_type = 'application/json',
            )


class WhoAmI(View):

    def get(self, request):
        response = HttpResponse()
        if request.user.is_authenticated:
            response.write(request.user.username)
        else:
            response.write('user is none')
        return response