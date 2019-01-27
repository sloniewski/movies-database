from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views

app_name = 'users'

urlpatterns = [

    path('token-auth/', obtain_auth_token, name='token-auth'),

    path('login/', views.LoginApiView.as_view(), name='session-login'),

    path('whoami/', views.WhoAmI.as_view(), name='whoami'),

]