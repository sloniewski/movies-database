from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from users import views

app_name = 'users'

router = routers.SimpleRouter()
router.register(
    'watchlist',
    views.WatchListView,
    base_name='watchlist',
)

urlpatterns = [

    path('token-auth/', obtain_auth_token, name='token-auth'),

    path('login/', views.LoginApiView.as_view(), name='session-login'),

    path('whoami/', views.WhoAmI.as_view(), name='whoami'),

]

urlpatterns += router.urls
