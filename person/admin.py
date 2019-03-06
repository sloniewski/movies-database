from django.contrib import admin
from django.contrib.admin import ModelAdmin

from person.models import Person


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    readonly_fields = ['slug']
