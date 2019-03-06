from django.contrib import admin
from django.contrib.admin import ModelAdmin

from movie.models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(ModelAdmin):
    readonly_fields = [
        'slug'
    ]


admin.site.register(Genre)
