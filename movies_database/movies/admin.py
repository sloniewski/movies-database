# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from movies.models import Movie, Role

admin.site.register(Movie)
admin.site.register(Role)
