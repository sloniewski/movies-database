from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token

from main.utils import generate_slug
from main.models import TimeStampMixin
from movie.models import Movie


class CustomUser(AbstractUser):

    def get_token(self):
        return Token.objects.get(user=self)


class RatingScore(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings',
    )
    value = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Ratings'
        unique_together = [
            ('user', 'movie')
        ]

    def __str__(self):
        return 'user:{} score:{}'.format(self.user.username, self.value)


class WatchList(TimeStampMixin, models.Model):
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
        verbose_name_plural = 'Watchlist entries'

    def __str__(self):
        return 'List:{} {}'.format(self.list.id, self.movie.title)
