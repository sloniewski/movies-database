from django.db import models
from django.contrib.auth.models import AbstractUser

from movie.models import Movie


class CustomUser(AbstractUser):
    pass


class RatingScore(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    value = models.PositiveIntegerField(null=True)


class WatchList(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    movies = models.ManyToManyField(
        Movie
    )
