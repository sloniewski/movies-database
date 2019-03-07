from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from users.models import (
    CustomUser,
    WatchListEntry,
    WatchList,
    RatingScore,
)


@admin.register(RatingScore)
class RatingAdmin(ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(WatchListEntry)
class WatchListEntryAdmin(ModelAdmin):
    pass


@admin.register(WatchList)
class WatchListAdmin(ModelAdmin):
    readonly_fields = ['slug']
