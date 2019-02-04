from django.shortcuts import reverse
from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def movies_list_url(self):
        return reverse('genre-movie-list', kwargs={'pk': self.pk})


class Movie(models.Model):
    title = models.CharField(
        max_length=64,
    )
    description = models.TextField()

    year = models.IntegerField()
    genre = models.ManyToManyField(
        Genre,
    )
    rating = models.IntegerField(
        null=True,
        blank=True,
    )

    @property
    def director(self):
        directors_queryset = self.crew.filter(credit='director')
        res = []
        for director in directors_queryset:
            res.append(director.fullname)
        return res

    @property
    def url(self):
        return reverse('movie:movie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.title, self.year)
