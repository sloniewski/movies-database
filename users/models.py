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

    def __str__(self):
        return '{} {}'.format(self.user.username, self.name)


class WatchListEntry(models.Model):
    list = models.ForeignKey(
        WatchList,
        on_delete=models.CASCADE,
        related_name='entries',
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [
            ('list', 'movie'),
        ]

    def __str__(self):
        return 'List:{} {}'.format(self.list.id, self.movie.title)
