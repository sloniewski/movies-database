"""movies_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from person.urls import router as person_router
from movie.urls import router as movie_router
from part.urls import router as part_router
from users.urls import router as users_router


router = DefaultRouter()
router.registry.extend(person_router.registry)
router.registry.extend(movie_router.registry)
router.registry.extend(part_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/<version>/', include(router.urls)),

    path('api/users/', include('users.urls'))

]
