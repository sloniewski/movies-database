from django.urls import include, path, register_converter
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from person.urls import router as person_router
from movie.urls import router as movie_router
from part.urls import router as part_router
from users.urls import router as users_router


class Version:
    regex = 'v[0-9]{1,2}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


register_converter(converter=Version, type_name='version')


router = DefaultRouter()
router.registry.extend(person_router.registry)
router.registry.extend(movie_router.registry)
router.registry.extend(part_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/<version:version>/', include(router.urls)),

    path('api/users/', include('users.urls'))

]
