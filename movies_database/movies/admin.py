# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from movies.models import Movie, Genre, Cast, Crew


admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Genre)
