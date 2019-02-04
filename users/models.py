from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

from main.utils import generate_slug
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
    slug = models.SlugField(
        unique=True,
        null=True,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        generate_slug(instance=self)
        return super().save(*args, **kwargs)

    @property
    def url(self):
        return reverse('users:watchlist-detail', kwargs={'slug': self.slug})


class WatchListEntry(models.Model):
    list = models.ForeignKey(
        WatchList,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )

