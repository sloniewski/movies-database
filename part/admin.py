from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Cast, Crew

@admin.register(Cast)
class CastAdmin(ModelAdmin):
    pass


@admin.register(Crew)
class CrewAdmin(ModelAdmin):
    pass